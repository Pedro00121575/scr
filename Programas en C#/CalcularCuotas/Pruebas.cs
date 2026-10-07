

public class Pruebas
{
    public static void PruebasMostrar()
    
{
decimal saldo = 1000;
decimal tasamensual = 0.01m;
decimal cuota = 340;

for (int i = 1; i <= 3; i++)
{
    decimal interes = saldo * tasamensual;
    decimal abono = cuota - interes;
    saldo = saldo - abono;

    Console.WriteLine(i + " | " + interes + " | " + abono + " | " + saldo);
}

 }}