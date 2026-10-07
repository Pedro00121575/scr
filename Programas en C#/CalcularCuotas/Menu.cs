using System.Runtime.InteropServices.Marshalling;
using Spectre.Console;

public class MenuInicio {
   
    public static string MostrarMenu()
    {
        AnsiConsole.Clear();


        var panel = new Panel("[bold yellow]Menú de préstamos y gestión financiera[/]")
            .Header("")
            .RoundedBorder();
        ///    .Expand(); // Hace que ocupe todo el ancho de la consola si lo deseas



        AnsiConsole.Write(panel);

    var choice = AnsiConsole.Prompt(
        new SelectionPrompt<string>()
            .Title("Seleciona lo que quieres hacer:")
            .AddChoices("Hacer prestamos", "Ver intereses fijos", "Salir"));
            

            AnsiConsole.MarkupLine($"Procesando [red]{choice}[/]");
            AnsiConsole.Write(panel);
                return choice;
        
            
        
        
        }    
               
    }
