import os
import shutil
import time
from colorama import init, Fore, Back, Style
import argparse

init()

output_path = os.path.join(os.path.expanduser("~"), "Desktop")

parser = argparse.ArgumentParser(prog="organizer.py", description="organize files", epilog="example: python organizer.py --path C:/Users/Desktop")
parser.add_argument("-p", "--path", help=f"source Path to Files directory e.g {output_path}")

args = parser.parse_args()


def main(src_path):
	# banner
	print(Fore.BLACK + Back.WHITE + f"***************(File Organizer)***************" + Style.RESET_ALL)
	print(Fore.BLACK + Back.WHITE + f"   By Sys_br3ach3r                            " + Style.RESET_ALL)

	# dictionary
	folders = {
		"pictures" : ["png", "jpg", "jpeg"],
		"documents": ["pdf", "docx", "xlsx", "txt", "ppt"],
		"archives": ["zip", "7z", "rar", "tar", "gz", "bz2", "dmg", "tgz", "xz", "iso", "cpio"],
		"audio": ["wav", "mp3", "aac", "flac", "ogg", "wma", "m4a", "aiff", "amr"],
		"videos" : ["mkv", "mp4"],
		"programming" : ["py", "ino", "html", "sh", "cbp"],
		# "others" : []
	}

	# get files from specified directory
	try:
		files = os.listdir(src_path)
	except Exception as e:
		print(f" {Fore.RED}Error:{Style.RESET_ALL} {e}")
		quit()

	# loading
	print(f" {Fore.RED}Warning: This will overwrite existing files.{Style.RESET_ALL}")
	for interval in range(0, 101):
		print(f"\r  Sorting Files:{Fore.LIGHTCYAN_EX} {interval}% {Style.RESET_ALL}", end="")
		time.sleep(0.1)

	# use key and value to sort files into respective folders
	for key in folders:
		for value in folders[key]:
			# get extension
			for file in files:
				try:
					get_extension = file.split(".")
					extension = get_extension[1]

					# control statement i.e. if file is found
					if value in extension:
						dest_dir = output_path + "/Organized" + "/" + key + "/" + value

						# make directory
						os.makedirs(dest_dir, exist_ok=True)

						# move files. will overwrite existing file due to specifying full dest path + filename
						shutil.move(os.path.join(src_path, file), os.path.join(dest_dir, file))

						# file location
						print(f" {Fore.LIGHTGREEN_EX}[+]{Style.RESET_ALL} {dest_dir}/{file}")

					else: # if extension is unknown
						pass

				except IndexError: # if extension is not found
					pass

	print(f"\n{Fore.BLACK + Back.WHITE}     Files sorted Successfully.               " + Style.RESET_ALL)


if __name__ == "__main__":
	try:
		main(src_path=args.path)

	except KeyboardInterrupt:
		abort_countdown = [5, 4, 3, 2, 1]
		for count in abort_countdown:
			print(f"\r ({Fore.RED}Ctrl + c{Style.RESET_ALL}) Aborting in {count}", end="")
			time.sleep(0.5)
		quit()
