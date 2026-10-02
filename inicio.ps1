# --- ARCHIVO: inicio.ps1 ---
Write-Host ">>> Conectado a mi Servidor Cloud en PowerShell <<<" -ForegroundColor Cyan

# 1. Función para instalar un programa rápido (Ejemplo: Google Chrome)
function Instalar-Chrome {
    Write-Host "Instalando Google Chrome..." -ForegroundColor Yellow
    $Path = "$env:TEMP\ChromeStandaloneSetup64.exe"
    Invoke-WebRequest -Uri "https://google.com" -OutFile $Path
    Start-Process -FilePath $Path -Args "/silent /install" -Wait
    Write-Host "¡Chrome instalado con éxito!" -ForegroundColor Green
}

# 2. Función para ver tus notas guardadas
function Ver-Notas {
    Write-Host "--- MIS NOTAS RÁPIDAS ---" -ForegroundColor Magenta
    # Esto leerá otro archivo de texto que subas a tu GitHub
    irm "https://githubusercontent.com"
}

# Creamos alias cortos para usarlos rápido en la consola ajena
Set-Alias -Name ichrome -Value Instalar-Chrome
Set-Alias -Name notas -Value Ver-Notas

Write-Host "Comandos cargados: 'ichrome' para instalar Chrome, 'notas' para ver tus apuntes." -ForegroundColor Green
