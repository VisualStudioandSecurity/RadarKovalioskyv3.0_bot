# 1. Definições de Segurança
$data = Get-Date -Format "yyyy-MM-dd_HH-mm"
$backupPath = "../backups_trading"
if (-not (Test-Path $backupPath)) { New-Item -ItemType Directory -Path $backupPath }

# 2. Compactação dos arquivos críticos (Dashboard e Backend)
Write-Host "📦 Iniciando Backup de Segurança..." -ForegroundColor Cyan
Compress-Archive -Path "server.js", "dashboard.html", ".env", "package.json" -DestinationPath "$backupPath/backup_$data.zip" -Force

# 3. Fluxo do Git com Força (Sincronização Final)
Write-Host "🚀 Enviando para o GitHub..." -ForegroundColor Green
git add .
git commit -m "feat: atualização segura com backup local em $data"
git push -u origin main --force

Write-Host "✅ Processo Concluído! Backup salvo em $backupPath" -ForegroundColor Green
