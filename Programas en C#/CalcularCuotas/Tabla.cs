using System.Runtime.InteropServices.Marshalling;
using Spectre.Console;

public class Manejadortablas
{
    public static void mostrartablas()
    {

        // Styled text with markup

        AnsiConsole.MarkupLine("[bold blue]Bienbenido[/] a [green]Tabla de interes Fijo[/]!");

    var tabla = new Table();


        tabla.Border(TableBorder.Rounded);
        tabla.AddColumn(".",col => col.Centered());
        tabla.AddColumn(".");
        tabla.AddColumn(".");
        tabla.AddColumn(".");
        tabla.AddColumn(".");
        tabla.AddRow("Mosntos interes","2.5%","5%","7.5%","10%");

    AnsiConsole.Write(tabla);
    
    
    }
}
