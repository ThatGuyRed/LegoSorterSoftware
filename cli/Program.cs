using System;
using System.Diagnostics;
using System.IO;
namespace cli;

class Program
{

  static void Main(string[] args)
  {
    const string command = "python 'Brickognize with Custom Dictionary.py'";

    Process proc = new Process();
    proc.StartInfo.FileName = Utilities.Terminal();
    proc.StartInfo.UseShellExecute = true;
    proc.StartInfo.CreateNoWindow = false;
    proc.StartInfo.WorkingDirectory = Directory.GetParent(Environment.CurrentDirectory).FullName;
    proc.StartInfo.Arguments = $"-c \"{command}\"";
    proc.Start();
    proc.WaitForExit();

  }
}
