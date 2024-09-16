#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import ...



def main():
  os.environ.setdefault('DJANNGO_SETTINGS_MODULE', 'taskmanager.settings')
  try:
    from django.core.management import execute_from_command_line 
except ImportError as exc:
    raise ImportError(
      "Couldn't import Dgango. Are you sure it's installed and "
      "available on your PYTHONPATH environment variable"
      "forget to activate a virtualisierung environment?"
    ) from exc
execute_from_command_line(sys.argv)


if __name__ == '__main__':
  main()
