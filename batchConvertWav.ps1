Get-ChildItem *.wav -recurse | % { ffmpeg.exe -i $_.FullName (".\_converted" + "\" +$_.Name) }
