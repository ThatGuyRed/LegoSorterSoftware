using System;
using System.Runtime.InteropServices;
using System.Diagnostics;
namespace cli;

class Utilities
{
  internal static string Terminal()
  {
    if (RuntimeInformation.IsOSPlatform(OSPlatform.Windows)) { return "cmd.exe"; }
    else if (RuntimeInformation.IsOSPlatform(OSPlatform.Linux)) { return "/bin/bash"; }
    else { return "undefined"; }
  }
}

