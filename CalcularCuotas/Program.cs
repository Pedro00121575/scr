using System.Runtime.InteropServices.Marshalling;
using Spectre;
using Spectre.Console;


var fname =  AnsiConsole.Ask<string>("Pontu nombre");
var lname = AnsiConsole.Ask<string>("Pontu apellido");
var edad = AnsiConsole.Ask<int>("Pontu edad");

if (edad >= 18) { 
    AnsiConsole.MarkupLine($"[green]Que bueno eres mayor de edad Procediendo......[/]");
    

}
 
else 
{
    AnsiConsole.MarkupLine($"[red]Que mal aun no cumples los requisitod de edad Deteniendo el proceso......[/]");
    return;
}


var montoprest = AnsiConsole.Ask<double>("Dime el primer monto del prestamo:");
var tiempoprest = AnsiConsole.Ask<int>("Dime el tiempo del prestamo:");

var cuotadia = montoprest / tiempoprest;


AnsiConsole.MarkupLine($"Tu nombre es: [blue]{fname}[/], y tu apellido es {lname} , y tu tienes {edad} años de edad");
AnsiConsole.MarkupLine($"Este es el monto de tu prestamo de [red]{montoprest}[/], pesos dominicanos y el tiempo es de [red]{tiempoprest}[/] dias aproximados,");
AnsiConsole.MarkupLine($"Este sera [red]{cuotadia}[/] ,la cuota diaria de tu prestamo ");
