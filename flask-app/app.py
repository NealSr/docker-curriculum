from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
  "http://www.nasa.gov/sites/default/files/thumbnails/image/iss043e093480_lrg.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/esp_044675_2580.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/nhq201607070004.jpg.jpeg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/28080162595_65d5012e24_o.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/27997163342_4ea08a0abc_o.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/pia20706_figb_labeled.png",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/27392354164_7912311d8c_o.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/iss048e007924.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/27263296274_db0774f7be_o.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/27928160046_309a2b0123_o.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/pia20701.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/m16-055a.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/hs-2016-22-b-full.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/antarctica_oli_2015061_lrg.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/iss048e004418.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/27490491440_d820b1ecff_o.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/sceptor_city_nasa_half_res.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/27041570914_5de6cc0400_o.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/27594170151_e2625a7d6b_o.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/lrc-2016-h1_p_orion-060712.jpeg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/ksc-20160613-ph_kls0001_0016.jpeg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/hubble_friday_06102016.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/27250243350_5563fbc72b_o.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/image_2_nicer.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/27002215442_179da57f4b_o.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/27420333805_6fd1876a46_o.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/hubble_friday_06032016.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/darksideimage_unann.png",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/pia13500.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/iss045e056257_lrg.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/27197314521_68a25511c9_o.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/mars_polar_deposits_main.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/ksc-20160521-ph_dng0001_0066.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/violinglacier.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/pia20481-1041.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/26512620163_904c1a34f8_o.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/sts101-s-007.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/iss047e122077a.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/iss044e045215_lrg.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/dss35c.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/hubble_friday_05132016.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/13173526_1000776189999401_5564117112764344623_o.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/26882201861_d4419bc21e_o.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/canada.a2016130.1915.500m_0.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/26844814011_363ee0e023_o.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/hubble_friday_05062016.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/9460616788_d08d4ae81b_o.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/esp_044662_2010.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/13112898_566270633555768_80769708423810417_o.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/pia18368-1041.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/26602405532_773fcfaf09_o.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/26578355561_bd617abb78_o.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/pia20332-figa_sol1302_ml_mcam06191_w_labels-cr.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/pia20645_main.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/tyuleniy_oli_2016097_lrg_a.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/jsc2016e032858.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/sep_contract_award_hall_thruster.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/26524351635_5579dbcb71_o.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/dsc_1124_0.jpg",
  "http://www.nasa.gov/sites/default/files/thumbnails/image/pia18366-1041.jpg"
]

@app.route('/')
def index():
  url = random.choice(images)
  number = images.index(url)
  return render_template('index.html', url=url, number=number)

if __name__ == "__main__":
  app.run(host="0.0.0.0")
