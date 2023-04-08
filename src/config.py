##
## interrupt parameters for geiger probe
##
gpiochip="/dev/gpiochip0"		# gpio chip name
geiger_gpioline=6			# gpio port for imput GPIO4
geiger_measure_int=60			# measurement time interval
divider=151.3 				# divider to calculate uSiviert from CPM (valid for geiger_measure_int=60

##
## parameters for geiger DB record
##
url="http://localhost:8086"
org="geiger"
bucket="geiger"
token="admin:admin"
timeout=6000
verify_ssl=False
point="geiger"
location="Slovensko"
machine=""
ipaddr=""
macaddr=""
hostname="geiger_bananapi"