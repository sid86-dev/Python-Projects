import time
import psutil
from rich.console import Console

console = Console()

console.print(f"\nMemory: {psutil.virtual_memory()}\n", style='bold red')

last_receive = psutil.net_io_counters().bytes_recv

last_sent = psutil.net_io_counters().bytes_sent

last_total = last_receive + last_sent

while True:

	bytes_received = psutil.net_io_counters().bytes_recv
	bytes_sent = psutil.net_io_counters().bytes_sent

	bytes_total = bytes_sent + bytes_received

	new_received = bytes_received - last_receive
	new_sent = bytes_sent - last_sent

	new_total = bytes_total - last_total

	mb_new_received = new_received / 1024 / 1024
	mb_new_sent = new_sent / 1024 / 1024
	mb_new_total = new_total / 1024 / 1024

	console.print(f"{mb_new_received:.2f} MB received	|	{mb_new_sent:.2f} MB sent 		|	{mb_new_total:.2f} MB total", style="green")

	last_receive = bytes_received
	last_sent = bytes_sent
	last_total = bytes_total

	time.sleep(2)