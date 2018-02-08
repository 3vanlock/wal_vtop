import os.path
import json

# wal_vtop details
VERSION = 0.1.1

# Get path for colors.json from ~/.cache/wal/colors.json
HOME_DIR = os.getenv("HOME", os.getenv("USERPROFILE"))
WAL_PATH = os.path.join(HOME_DIR, ".cache/wal")
WAL_FILE = "colors.json"
# Get path for vtop themes
VTOP_PATH = "/usr/lib/node_modules/vtop/themes"
VTOP_FILE = "wal.json"
WAL = os.path.join(WAL_PATH, WAL_FILE)
VTOP = os.path.join(VTOP_PATH, VTOP_FILE)

# Open colors.json and load
wal_colors = json.load(open(WAL))

# Transfer wal colors to vtop theme json scheme
walj = {
	"name": "Wal",
	"author": "epl",
	"title": {
		"fg": wal_colors['colors']['color1']
	},
	"chart": {
		"fg": wal_colors['colors']['color1'],
		"border": {
			"type": "line",
			"fg": wal_colors['colors']['color1']
		}
	},
	"table": {
		"fg": wal_colors['colors']['color15'],
		"items": {
			"selected": {
				"bg": wal_colors['colors']['color1'],
				"fg": wal_colors['colors']['color15']
			},
			"item": {
				"bg": wal_colors['colors']['color15'],
				"fg": wal_colors['colors']['color1']
			}
		},
		"border": {
			"type": "line",
			"fg": wal_colors['colors']['color1']
		}
	},
	"footer": {
		"fg": wal_colors['colors']['color1']
	}
}

# Write theme json to vtop themes directory
with open(VTOP, 'w') as f:
    json.dump(walj, f)
