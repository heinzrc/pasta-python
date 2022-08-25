from flask import Flask, render_template, jsonify
import alert
import sys
sys.path.append('/home/pi/PyMLX90614-0.0.3/mlx90614') 
from smbus2 import SMBus
from mlx90614 import MLX90614

flag = 0
bus = SMBus(0)
sensor = MLX90614(bus, address=0x5A)

app = Flask(__name__)
@app.route("/")
def main():
   user = 'User'
   templateData = {
      'title' : 'Project Pasta',
      'user': user
      }
   return render_template('index.html', **templateData)

@app.route('/update_text', methods=['POST'])
def read_temp():
	global flag
	while True:
		temp_c = float(sensor.get_object_1())
		#temp_f = temp_c * 9.0 / 5.0 + 32.00
		if temp_c >= 80.00:
			if flag == 0:
				flag = 1
				alert.alert_phone()
		else:
			flag = 0
		return jsonify('', render_template('temp_out.html',temp=format(temp_c, '.2f')))

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=False)
