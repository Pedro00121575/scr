using System.ComponentModel.DataAnnotations.Schema;
using System.Runtime.InteropServices;
using System.Runtime.InteropServices.Marshalling;
using Spectre.Console;



///string selecion = MenuInicio.MostrarMenu();

///switch(selecion)

//{
//    case "hacer prestamos":


///inicio crear prestamo
AnsiConsole.Clear();


AnsiConsole.Status()
    .Start("Procesando...", ctx =>
    {Thread.Sleep(2000);
        
    });
AnsiConsole.MarkupLine("[green]Iniciando.....[/]");


///Variables de captura de mis datos 
var fname =  AnsiConsole.Ask<string>("Pontu nombre");
var lname = AnsiConsole.Ask<string>("Pontu apellido");
var edad = AnsiConsole.Ask<int>("Pontu edad");


///Condicional para que no exeda el limite de esdad permitido 
if (edad >= 18) { 
    AnsiConsole.MarkupLine($"[green]Que bueno eres mayor de edad Procediendo......[/]");
    
}
 else 
{
    AnsiConsole.MarkupLine($"[red]Que mal[/] [green]{fname}[/] [red]pero aun no cumples los requisitod de edad, Deteniendo el proceso......[/]");
    return;
}

///Variable que almacena los prestamos  
decimal montoprestamo = AnsiConsole.Ask<decimal>("Dime el monto del prestamo:");
int tiempoprestamo = AnsiConsole.Ask<int>("Dime el tiempo del prestamo:");
decimal tasaInteresAnual = AnsiConsole.Ask<decimal>("Dime cual es la tasa de interes ");



/// Variable para la tasas de interesde  mes / Año
var tasaInteresMensual = tasaInteresAnual / 12 / 100;

// (1 + i)^n: se calcula una sola vez y se reutiliza
decimal factor = (decimal)Math.Pow((double)(1 + tasaInteresMensual), tiempoprestamo);

// C = M * i * factor / (factor - 1)
decimal cuotaFija = montoprestamo * tasaInteresMensual * factor / (factor - 1);


///variable para calcular y mostrar en pantalla el monto total 
var CantidadCuotafija = cuotaFija * tiempoprestamo;


/// saldo pendiente del prestamo 
var Saldo = montoprestamo ;









var table = new Table ().ShowRowSeparators() .Title("[green]Tabla de Amortizacion[/]");

table.AddColumns(
    new TableColumn("No. de cuota").Centered(),
    new TableColumn("Pago de cuota Fija").Centered(),
    new TableColumn("Interés a pagar").Centered(),
    new TableColumn("Abono a capital").Centered(),
    new TableColumn("Saldo").Centered()
);


decimal Totalinteres = 0;

for(int i = 1; i <= tiempoprestamo; i++)
{

// Otra variable para dar el total del interes
var Interes = Saldo * tasaInteresMensual;
var abono = cuotaFija - Interes;
Saldo = Saldo - abono;



table.AddRow($"{i}", $"{cuotaFija:c2}",$"{Interes:c2}",$"{abono:c2}",$"{Saldo:c2}");
}

table.AddRow($"Total a pagar",$"[green]{CantidadCuotafija:c2}[/]",$"[green]{Totalinteres:c2}[/]",$"[green]{Totalinteres:c2}[/]",$"[green]{Totalinteres:c2}[/]");
 








AnsiConsole.Write(table);
///{
    
    
    ///}

///return;
///Fin crear prestamo


   /// case "Ver intereses fijos":
    


     
    
    ///return;

    ///case "salir":
 
  
    
    ///return;



///}

 
