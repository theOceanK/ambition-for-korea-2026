param([Parameter(Mandatory)][string]$In, [Parameter(Mandatory)][string]$Out)
$ErrorActionPreference = 'Stop'
$inPath = (Resolve-Path -LiteralPath $In).Path
$outPath = [System.IO.Path]::GetFullPath($Out)
$pp = New-Object -ComObject PowerPoint.Application
try {
    # ReadOnly, Untitled=false, WithWindow=false
    $pres = $pp.Presentations.Open($inPath, -1, 0, 0)
    $pres.SaveAs($outPath, 32)   # ppSaveAsPDF
    $pres.Close()
} finally {
    $pp.Quit()
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($pp) | Out-Null
}
Write-Output "pdf $outPath"
