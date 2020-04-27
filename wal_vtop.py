import os.path
import json
import sys
import argparse

# wal_vtop details
VERSION = "0.1.1"

# Get path for vtop themes
vtop_file = "wal.json"

def setConfig():
	# Get host OS
	hostOS = getOS()
	# Get user home directory
	home_dir = os.getenv("HOME", os.getenv("USERPROFILE"))
	# Set wal colors file
	wal_colors = os.path.join(home_dir, ".cache", "wal", "colors.json")
	# Confirm wal export exists
	if not os.path.isfile(wal_colors):
		# Print error and exit if not found
		print("Wal colors could not be found. Try running `wal` again")
		sys.exit(1)
	# Set vtop directory by platform
	if hostOS == "linux":
		vtop_path = "/usr/lib/node_modules/vtop/themes"
		vtop_theme = os.path.join(vtop_path, vtop_file)
	elif hostOS == "win32":
		print("Windows platform not supported")
		sys.exit(1)
	elif hostOS == "darwin":
                vtop_path = "/usr/local/lib/node_modules/vtop/themes"
                vtop_theme = os.path.join(vtop_path, vtop_file)
	else:
		# Print error and exit if OS unsupported
		print("Unsupported operating system")
		sys.exit(1)
	# Return file paths as strings for wal color file and vtop theme file
	return wal_colors, vtop_theme

def themeVtop(wal_colors_path, vtop_theme_path):
	# Open colors.json and load
	import_colors = json.load(open(wal_colors_path))

	# Transfer wal colors to vtop theme json scheme
	walj = {
		"name": "Wal",
		"author": "epl",
		"title": {
			"fg": import_colors['colors']['color1']
		},
		"chart": {
			"fg": import_colors['colors']['color1'],
			"border": {
				"type": "line",
				"fg": import_colors['colors']['color1']
			}
		},
		"table": {
			"fg": import_colors['colors']['color15'],
			"items": {
				"selected": {
					"bg": import_colors['colors']['color1'],
					"fg": import_colors['colors']['color15']
				},
				"item": {
					"fg": import_colors['colors']['color1']
				}
			},
			"border": {
				"type": "line",
				"fg": import_colors['colors']['color1']
			}
		},
		"footer": {
			"fg": import_colors['colors']['color1']
		}
	}

	# Write theme json to vtop themes directory
	try:
		with open(vtop_theme_path, 'w') as f:
			json.dump(walj, f)
		if os.path.isfile(vtop_theme_path):
			print("vtop theme written successfully. start vtop with `vtop --theme wal` to view")
	except:
		print("Error writing vtop theme file")
		sys.exit(1)

def getOS():
	# system call for user platform
	hostOS = sys.platform
	# return os as string: linux, win32, darwin
	return hostOS

def getArgs():
    # get the arguments with argparse
    description = "wal vtop"
    arg = argparse.ArgumentParser(description=description)

    arg.add_argument("-v", "--version", action="store_true",
            help="Print wal_vtop version.")

    return arg.parse_args()

def main():
	# Parse arguments
	arguments = getArgs()
	# Print app version
	if arguments.version:
		print("wal vtop", VERSION)
		sys.exit()
	# Set file paths
	wcp, vtp = setConfig()
	# Translate and write theme
	themeVtop(wcp, vtp)

if __name__ == '__main__':
	main()
