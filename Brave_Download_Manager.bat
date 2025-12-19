<# :
@echo off
title YT-DLP Manager (BRAVE404)

if "%~1" neq "" (cd /d "%~1") else (cd /d "%~dp0")
powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((Get-Content '%~f0') -join [Environment]::NewLine); Main"
exit /b
#>

Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

function Main {
    # --- CONFIG ---
    $scriptPath = Get-Location
    $ytDlpPath = Join-Path $scriptPath "yt-dlp.exe"
    $ffmpegPath = $null
    $outputDir = Join-Path $scriptPath "Hasil Download"
    
    # Check Tools
    if (-not (Test-Path $ytDlpPath)) {
        [System.Windows.Forms.MessageBox]::Show("Error: yt-dlp.exe tidak ditemukan!`nSilakan download yt-dlp.exe dan taruh di folder yang sama.", "File Missing", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Error)
        exit
    }

    if (Test-Path (Join-Path $scriptPath "ffmpeg.exe")) { 
        $ffmpegPath = Join-Path $scriptPath "ffmpeg.exe" 
    } else {
        $found = Get-ChildItem -Path $scriptPath -Filter "ffmpeg.exe" -Recurse -Depth 2 -ErrorAction SilentlyContinue | Select-Object -First 1
        if ($found) { $ffmpegPath = $found.FullName }
    }
    
    if (-not (Test-Path $outputDir)) { New-Item -ItemType Directory -Force -Path $outputDir | Out-Null }

    # --- GUI FORM (MODERN THEME) ---
    $form = New-Object System.Windows.Forms.Form
    $form.Text = "Powered by yt-dlp | Modified by Brave404"
    $form.Size = New-Object System.Drawing.Size(640, 490) # Compact Height
    $form.StartPosition = "CenterScreen"
    $form.FormBorderStyle = "FixedSingle"
    $form.MaximizeBox = $false
    $form.BackColor = [System.Drawing.Color]::FromArgb(30, 30, 35) # Dark Charcoal
    $form.ForeColor = [System.Drawing.Color]::WhiteSmoke
    $mainFont = New-Object System.Drawing.Font("Segoe UI", 10)
    $headerFont = New-Object System.Drawing.Font("Segoe UI", 14, [System.Drawing.FontStyle]::Bold)
    $form.Font = $mainFont

    # Header Panel REMOVED

    # REMOVED Title Label as requested

    # Label URL
    $lblUrl = New-Object System.Windows.Forms.Label
    $lblUrl.Text = "YouTube URL:"
    $lblUrl.Location = New-Object System.Drawing.Point(25, 20)
    $lblUrl.AutoSize = $true
    $lblUrl.ForeColor = [System.Drawing.Color]::LightGray
    $form.Controls.Add($lblUrl)

    # Input URL
    $txtUrl = New-Object System.Windows.Forms.TextBox
    $txtUrl.Location = New-Object System.Drawing.Point(25, 45)
    $txtUrl.Size = New-Object System.Drawing.Size(430, 26)
    $txtUrl.BackColor = [System.Drawing.Color]::FromArgb(50, 50, 50)
    $txtUrl.ForeColor = [System.Drawing.Color]::White
    $txtUrl.BorderStyle = "FixedSingle"
    $form.Controls.Add($txtUrl)

    # Button Analyze
    $btnCheck = New-Object System.Windows.Forms.Button
    $btnCheck.Text = "CEK VIDEO"
    $btnCheck.Location = New-Object System.Drawing.Point(470, 43)
    $btnCheck.Size = New-Object System.Drawing.Size(130, 30)
    $btnCheck.BackColor = [System.Drawing.Color]::Black # Brave Black
    $btnCheck.ForeColor = [System.Drawing.Color]::White
    $btnCheck.FlatStyle = "Flat"
    $btnCheck.FlatAppearance.BorderSize = 1
    $btnCheck.FlatAppearance.BorderColor = [System.Drawing.Color]::Red
    $btnCheck.Cursor = [System.Windows.Forms.Cursors]::Hand
    $form.Controls.Add($btnCheck)

    # Combo Resolution
    $lblRes = New-Object System.Windows.Forms.Label
    $lblRes.Text = "Pilih Kualitas:"
    $lblRes.Location = New-Object System.Drawing.Point(25, 95)
    $lblRes.AutoSize = $true
    $lblRes.ForeColor = [System.Drawing.Color]::LightGray
    $form.Controls.Add($lblRes)

    $cmbRes = New-Object System.Windows.Forms.ComboBox
    $cmbRes.Location = New-Object System.Drawing.Point(140, 92)
    $cmbRes.Size = New-Object System.Drawing.Size(200, 26)
    $cmbRes.DropDownStyle = "DropDownList"
    $cmbRes.BackColor = [System.Drawing.Color]::FromArgb(50, 50, 50)
    $cmbRes.ForeColor = [System.Drawing.Color]::White
    $cmbRes.FlatStyle = "Flat"
    $form.Controls.Add($cmbRes)

    # Button Download
    $btnDL = New-Object System.Windows.Forms.Button
    $btnDL.Text = "DOWNLOAD SEKARANG"
    $btnDL.Location = New-Object System.Drawing.Point(360, 90)
    $btnDL.Size = New-Object System.Drawing.Size(240, 32)
    $btnDL.BackColor = [System.Drawing.Color]::DarkRed # Brave Red
    $btnDL.ForeColor = [System.Drawing.Color]::White
    $btnDL.Font = New-Object System.Drawing.Font("Segoe UI", 10, [System.Drawing.FontStyle]::Bold)
    $btnDL.Enabled = $false
    $btnDL.FlatStyle = "Flat"
    $btnDL.FlatAppearance.BorderSize = 0
    $btnDL.Cursor = [System.Windows.Forms.Cursors]::Hand
    $form.Controls.Add($btnDL)

    # Log Output
    $txtLog = New-Object System.Windows.Forms.TextBox
    $txtLog.Location = New-Object System.Drawing.Point(25, 140)
    $txtLog.Size = New-Object System.Drawing.Size(575, 250) # Reduced height slightly
    $txtLog.Multiline = $true
    $txtLog.ScrollBars = "Vertical"
    $txtLog.ReadOnly = $true
    $txtLog.BackColor = [System.Drawing.Color]::FromArgb(20, 20, 20)
    $txtLog.ForeColor = [System.Drawing.Color]::LimeGreen
    $txtLog.Font = New-Object System.Drawing.Font("Consolas", 10)
    $txtLog.BorderStyle = "None"
    $txtLog.Text = "Selamat Datang di YT-DLP Manager by BRAVE404`r`nSiap menunggu perintah..."
    $form.Controls.Add($txtLog)

    # Footer
    $lblFooter = New-Object System.Windows.Forms.Label
    $lblFooter.Text = "Powered by yt-dlp | Modified by Brave404"
    $lblFooter.Location = New-Object System.Drawing.Point(25, 420) # Fixed Position (Up)
    $lblFooter.AutoSize = $true
    $lblFooter.ForeColor = [System.Drawing.Color]::DimGray
    $lblFooter.Font = New-Object System.Drawing.Font("Segoe UI", 8)
    $form.Controls.Add($lblFooter)

    # --- EVENTS ---

    # Helper: Log
    $Log = {
        param($msg)
        $txtLog.AppendText("`r`n$msg")
        $txtLog.SelectionStart = $txtLog.Text.Length
        $txtLog.ScrollToCaret()
        $form.Refresh()
    }

    $btnCheck_Click = {
        $url = $txtUrl.Text
        if ([string]::IsNullOrWhiteSpace($url)) { $Log.Invoke("Error: URL Kosong!"); return }
        
        $btnCheck.Enabled = $false
        $btnDL.Enabled = $false
        $form.Cursor = [System.Windows.Forms.Cursors]::WaitCursor
        $cmbRes.Items.Clear()
        
        $Log.Invoke("[*] Menganalisa Video... Mohon Tunggu.")
        
        try {
            $cmd = "$ytDlpPath --dump-single-json `"$url`" --no-warnings"
            $json = Invoke-Expression $cmd 2>$null
            if (-not $json) { throw "Gagal ambil data" }
            $data = $json | ConvertFrom-Json
            
            $Log.Invoke("[+] Judul: $($data.title)")
            $Log.Invoke("[+] Channel: $($data.uploader)")
            
            $resList = @()
            foreach ($f in $data.formats) {
                if ($f.height -ne $null -and $f.vcodec -ne "none") {
                    if ($resList -notcontains $f.height) { $resList += $f.height }
                }
            }
            $resList = $resList | Sort-Object -Descending
            
            foreach ($r in $resList) { $cmbRes.Items.Add("Video ${r}p") }
            $cmbRes.Items.Add("Audio Only (MP3)")
            
            if ($cmbRes.Items.Count -gt 0) { 
                $cmbRes.SelectedIndex = 0 
                $btnDL.Enabled = $true
            }
            $Log.Invoke("[v] Analisa Selesai. Silakan Pilih Resolusi & Download.")
        } catch {
            $Log.Invoke("Error: Gagal menganalisa video. Cek koneksi/link.")
        } finally {
            $btnCheck.Enabled = $true
            $form.Cursor = [System.Windows.Forms.Cursors]::Default
        }
    }

    $btnDL_Click = {
        $sel = $cmbRes.SelectedItem
        if (-not $sel) { return }
        $url = $txtUrl.Text
        
        $btnDL.Enabled = $false
        $btnCheck.Enabled = $false
        
        $Log.Invoke("-------------------------------------")
        $Log.Invoke("PROGRESS DOWNLOAD DIMULAI...")
        $Log.Invoke("Target: $sel")
        $Log.Invoke("Please Wait... (Aplikasi akan freeze sebentar saat downloading)")
        $form.Refresh()

        $dlArgs = @()
        if ($ffmpegPath) { $dlArgs += "--ffmpeg-location `"$ffmpegPath`"" }
        $dlArgs += "-o `"$outputDir\%(title).100s.%(ext)s`""
        $dlArgs += "--no-mtime"
        # REMOVED --no-part (Possible cause of lock in GUI mode)
        $dlArgs += "--file-access-retries", "100"
        $dlArgs += "--no-continue"
        $dlArgs += "--force-overwrites"
        
        # FIX: Replace Special Characters (Safe & Clean Filename)
        # Quote the patterns because they go through CMD
        $dlArgs += "--replace-in-metadata", "title", "`"[&]`"", "and"
        $dlArgs += "--replace-in-metadata", "title", "`"[%]`"", "pct"
        $dlArgs += "--replace-in-metadata", "title", "`"[#]`"", "No."
        $dlArgs += "--replace-in-metadata", "title", "`"[\^]`"", "-"
        $dlArgs += "--replace-in-metadata", "title", "`"[$]`"", "S"

        if ($sel -eq "Audio Only (MP3)") {
            $dlArgs += "-f bestaudio/best --extract-audio --audio-format mp3"
        } else {
             $h = $sel -replace "\D","" # extract numbers
             $dlArgs += "-f `"bv*[height<=$h]+ba[ext=m4a]/bv*[height<=$h]+ba/b[height<=$h]`""
             $dlArgs += "--merge-output-format mp4"
             # REMOVED faststart to fix WinError 32 (File Lock)
        }
        
        $dlArgs += "`"$url`""
        
        # Robust Execution: Use CMD to handle quoting and merge stderr
        # We assume $ytDlpPath and arguments might have spaces
        $argString = $dlArgs -join " "
        $cmdArgs = "/c `"`"$ytDlpPath`" $argString 2>&1`""
        
        $pinfo = New-Object System.Diagnostics.ProcessStartInfo
        $pinfo.FileName = "cmd.exe"
        $pinfo.Arguments = $cmdArgs
        $pinfo.WorkingDirectory = $scriptPath # FIX: Explicitly set CWD
        $pinfo.RedirectStandardOutput = $true
        $pinfo.RedirectStandardError = $false # Merged above
        $pinfo.UseShellExecute = $false
        $pinfo.CreateNoWindow = $true
        
        $p = New-Object System.Diagnostics.Process
        $p.StartInfo = $pinfo
        $p.Start() | Out-Null
        
        while (-not $p.HasExited) {
            $line = $p.StandardOutput.ReadLine()
            if ($line) { $Log.Invoke($line) }
            [System.Windows.Forms.Application]::DoEvents()
        }
        $rest = $p.StandardOutput.ReadToEnd()
        if ($rest) { $Log.Invoke($rest) }
        
        $Log.Invoke("-------------------------------------")
        
        if ($p.ExitCode -eq 0) {
            $Log.Invoke("[v] DOWNLOAD SELESAI!")
            $Log.Invoke("File tersimpan di folder 'Hasil Download'")
        } else {
            $Log.Invoke("[!] DOWNLOAD GAGAL / ERROR")
            $Log.Invoke("Pastikan koneksi internet lancar & link benar.")
        }
        
        $btnDL.Enabled = $true
        $btnCheck.Enabled = $true
    }

    $btnCheck.Add_Click($btnCheck_Click)
    $btnDL.Add_Click($btnDL_Click)

    $form.Add_Shown({ $form.Activate() })
    [void] $form.ShowDialog()
}

