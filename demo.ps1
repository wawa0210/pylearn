start powershell -ArgumentList " -File C:\Project\pydemo\clidemo\demo2.ps1"

$count = 0

while ($count -lt 20) {
    echo 'hello the world! from demo1'
    Start-Sleep 1
    $count+=1
}