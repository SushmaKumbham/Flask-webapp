import requests

from flask import Flask, render_template,request




from flask_socketio import SocketIO

app = Flask(__name__)



app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)



@app.route('/codechat.html')
def codechat():
    return render_template('codechat.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)










@app.route('/')
def home():
    return render_template('home.html')
@app.route('/ts.html/')
def ts():
    return render_template('ts.html')
@app.route('/ap.html/')
def ap():
    return render_template('ap.html')

@app.route('/agtoday.html/')
def agtoday():
    return render_template('agtoday.html')
@app.route('/agtoday.html/price.html/')
def price():
    return render_template('price.html')

@app.route('/agtoday.html/soil.html/')
def soil():
    return render_template('soil.html')

@app.route('/agtoday.html/pun.html/')
def pun():
    return render_template('pun.html')
@app.route('/agtoday.html/communi.html/')
def communi():
    return render_template('communi.html')
@app.route('/agtoday.html/pest.html/')
def pest():
    return render_template('pest.html')
@app.route('/agtoday.html/foodcorp.html/')
def foodcorp():
    return render_template('foodcorp.html')








@app.route('/ap.html/ananthapur.html/')
def ananthapur():
    return render_template('ananthapur.html')

@app.route('/ap.html/chittor.html/')
def chittor():
    return render_template('chittor.html')


@app.route('/ap.html/kurnool.html/')
def k():
    return render_template('kurnool.html')

@app.route('/ap.html/nellore.html/')
def nellore():
    return render_template('nellore.html')

@app.route('/ap.html/westgodavari.html/')
def wg():
    return render_template('westgodavari.html')

@app.route('/ap.html/eastgodavari.html/')
def eg():
    return render_template('eastgodavari.html')

@app.route('/ap.html/guntur.html/')
def guntur():
    return render_template('guntur.html')

@app.route('/ap.html/krishna.html/')
def krishna():
    return render_template('krishna.html')

@app.route('/ap.html/vizianagaram.html/')
def vz():
    return render_template('vizianagaram.html')

@app.route('/ap.html/kadapa.html/')
def kadapa():
    return render_template('kadapa.html')

@app.route('/ap.html/prakasam.html/')
def prakasam():
    return render_template('prakasam.html')

@app.route('/ap.html/srikakulam.html/')
def srikakulam():
    return render_template('srikakulam.html')

@app.route('/ap.html/visakhapatnam.html/')
def vs():
    return render_template('visakhapatnam.html')



@app.route('/ap.html/ananthapur.html/groundnut.html')
def  aground():
    return render_template('groundnut.html')


@app.route('/ap.html/ananthapur.html/sunflower.html')
def  asun():
    return render_template('sunflower.html')

@app.route('/ap.html/ananthapur.html/paddy.html')
def  apaddy():
    return render_template('paddy.html')


@app.route('/ap.html/ananthapur.html/cotton.html')
def  acotton():
    return render_template('cotton.html')

@app.route('/ap.html/ananthapur.html/maize.html')
def  amaize():
    return render_template('maize.html')


@app.route('/ap.html/chittor.html/paddy.html')
def cpaddy():
    return render_template('paddy.html')
@app.route('/ap.html/chittor.html/ragi.html')
def cragi():
    return render_template('ragi.html')
@app.route('/ap.html/chittor.html/red gram.html')
def credgram():
    return render_template('red gram.html')
@app.route('/ap.html/chittor.html/sugarcane.html')
def csugar():
    return render_template('sugarcane.html')
@app.route('/ap.html/chittor.html/groundnut.html')
def cgroundnut():
    return render_template('groundnut.html')

@app.route('/ap.html/kurnool.html/paddy.html')
def kpaddy():
    return render_template('paddy.html')

@app.route('/ap.html/kurnool.html/jowar.html')
def kj():
    return render_template('jowar.html')
@app.route('/ap.html/kurnool.html/red gram.html')
def kredg():
    return render_template('red gram.html')
@app.route('/ap.html/kurnool.html/ragi.html')
def kragi():
    return render_template('ragi.html')
@app.route('/ap.html/kurnool.html/groundnut.html')
def kgn():
    return render_template('groundnut.html')


@app.route('/ap.html/nellore.html/paddy.html')
def npaddy():
    return render_template('paddy.html')

@app.route('/ap.html/nellore.html/cotton.html')
def nco():
    return render_template('cotton.html')

@app.route('/ap.html/nellore.html/bajra.html')
def nb():
    return render_template('bajra.html')

@app.route('/ap.html/nellore.html/jowar.html')
def nj():
    return render_template('jowar.html')

@app.route('/ap.html/nellore.html/red gram.html')
def nrg():
    return render_template('red gram.html')

@app.route('/ap.html/nellore.html/greengram.html')
def ngg():
    return render_template('greengram.html')

@app.route('/ap.html/nellore.html/groundnut.html')
def ngn():
    return render_template('groundnut.html')


@app.route('/ap.html/westgodavari.html/paddy.html')
def wgp():
    return render_template('paddy.html')

@app.route('/ap.html/westgodavari.html/sugarcane.html')
def wgsc():
    return render_template('sugarcane.html')

@app.route('/ap.html/westgodavari.html/maize.html')
def wgm():
    return render_template('maize.html')

@app.route('/ap.html/westgodavari.html/tobacco.html')
def wgt():
    return render_template('tobacco.html')

@app.route('/ap.html/westgodavari.html/greengram.html')
def wggg():
    return render_template('greengram.html')

@app.route('/ap.html/westgodavari.html/sunflower.html')
def wgsf():
    return render_template('sunflower.html')


@app.route('/ap.html/eastgodavari.html/bajra.html')
def egb():
    return render_template('bajra.html')

@app.route('/ap.html/eastgodavari.html/maize.html')
def egm():
    return render_template('maize.html')

@app.route('/ap.html/eastgodavari.html/red gram.html')
def egrg():
    return render_template('red gram.html')

@app.route('/ap.html/eastgodavari.html/greengram.html')
def eggg():
    return render_template('greengram.html')

@app.route('/ap.html/eastgodavari.html/bengalgram.html')
def egbg():
    return render_template('bengalgram.html')

@app.route('/ap.html/eastgodavari.html/sesame.html')
def egs():
    return render_template('sesame.html')

@app.route('/ap.html/eastgodavari.html/sugarcane.html')
def egsc():
    return render_template('sugarcane.html')

@app.route('/ap.html/guntur.html/cotton.html')
def gc():
    return render_template('cotton.html')


@app.route('/ap.html/guntur.html/maize.html')
def gm():
    return render_template('maize.html')


@app.route('/ap.html/guntur.html/chilli.html')
def gch():
    return render_template('chilli.html')

@app.route('/ap.html/guntur.html/paddy.html')
def gp():
    return render_template('paddy.html')




@app.route('/ap.html/krishna.html/paddy.html')
def krpaddy():
    return render_template('paddy.html')

@app.route('/ap.html/krishna.html/maize.html')
def krmaize():
    return render_template('maize.html')
@app.route('/ap.html/krishna.html/jowar.html')
def krjo():
    return render_template('jowar.html')
@app.route('/ap.html/krishna.html/cotton.html')
def krco():
    return render_template('cotton.html')
@app.route('/ap.html/krishna.html/sugarcane.html')
def krsc():
    return render_template('sugarcane.html')
@app.route('/ap.html/krishna.html/tobacco.html')
def krto():
    return render_template('tobacco.html')


@app.route('/ap.html/vizianagaram.html/paddy.html')
def vzp():
    return render_template('paddy.html')

@app.route('/ap.html/vizianagaram.html/cotton.html')
def vzco():
    return render_template('cotton.html')
@app.route('/ap.html/vizianagaram.html/bajra.html')
def vzba():
    return render_template('bajra.html')
@app.route('/ap.html/vizianagaram.html/ragi.html')
def vzra():
    return render_template('ragi.html')


@app.route('/ap.html/kadapa.html/paddy.html')
def kadapaddy():
    return render_template('paddy.html')

@app.route('/ap.html/kadapa.html/cotton.html')
def kadacotton():
    return render_template('cotton.html')

@app.route('/ap.html/kadapa.html/turmeric.html')
def kadaturmeric():
    return render_template('turmeric.html')

@app.route('/ap.html/kadapa.html/red gram.html')
def kadarg():
    return render_template('red gram.html')
@app.route('/ap.html/kadapa.html/coriander.html')
def kadacoriander():
    return render_template('coriander.html')

@app.route('/ap.html/prakasam.html/paddy.html')
def prpaddy():
    return render_template('paddy.html')
@app.route('/ap.html/prakasam.html/maize.html')
def prm():
    return render_template('maize.html')
@app.route('/ap.html/prakasam.html/jowar.html')
def prjo():
    return render_template('jowar.html')
@app.route('/ap.html/prakasam.html/cotton.html')
def prcotton():
    return render_template('cotton.html')
@app.route('/ap.html/prakasam.html/sugarcane.html')
def prsc():
    return render_template('sugarcane.html')
@app.route('/ap.html/prakasam.html/turmeric.html')
def prtu():
    return render_template('turmeric.html')
@app.route('/ap.html/prakasam.html/sesame.html')
def prse():
    return render_template('sesame.html')


@app.route('/ap.html/srikakulam.html/paddy.html')
def srip():
    return render_template('paddy.html')

@app.route('/ap.html/srikakulam.html/ragi.html')
def srira():
    return render_template('ragi.html')
@app.route('/ap.html/srikakulam.html/bajra.html')
def sriba():
    return render_template('bajra.html')



@app.route('/ap.html/visakhapatnam.html/paddy.html')
def vsp():
    return render_template('paddy.html')


@app.route('/ap.html/visakhapatnam.html/ragi.html')
def vsr():
    return render_template('ragi.html')
@app.route('/ap.html/visakhapatnam.html/jowar.html')
def vsjo():
    return render_template('jowar.html')
@app.route('/ap.html/visakhapatnam.html/bajra.html')
def vsba():
    return render_template('bajra.html')
@app.route('/ap.html/visakhapatnam.html/sugarcane.html')
def vssc():
    return render_template('sugarcane.html')






@app.route('/ts.html/warangalrural.html/')
def tswarangal():
    return render_template('warangalrural.html')

@app.route('/ts.html/warangalrural.html/paddy.html')
def tswarangalpad():
    return render_template('paddy.html')

@app.route('/ts.html/warangalrural.html/maize.html')
def tswarangalma():
    return render_template('maize.html')
@app.route('/ts.html/warangalrural.html/cotton.html')
def tswarangalcot():
    return render_template('cotton.html')
@app.route('/ts.html/warangalrural.html/groundnut.html')
def tswarangalgn():
    return render_template('groundnut.html')

@app.route('/ts.html/mahabubabad.html/')
def tsmahabubabad():
    return render_template('mahabubabad.html')
@app.route('/ts.html/mahabubabad.html/paddy.html')
def tsmahabubabadpaddy():
    return render_template('paddy.html')
@app.route('/ts.html/mahabubabad.html/maize.html')
def tsmahabubabadmaize():
    return render_template('maize.html')
@app.route('/ts.html/mahabubabad.html/cotton.html')
def tsmahabubabadcotton():
    return render_template('cotton.html')
@app.route('/ts.html/mahabubabad.html/groundnut.html')
def tsmahabubabadgn():
    return render_template('groundnut.html')
@app.route('/ts.html/jayashankarbhupalpally.html/')
def tsjb():
    return render_template('jayashankarbhupalpally.html')
@app.route('/ts.html/jayashankarbhupalpally.html/paddy.html')
def tsjbp():
    return render_template('paddy.html')
@app.route('/ts.html/jayashankarbhupalpally.html/maize.html')
def tsjbm():
    return render_template('maize.html')
@app.route('/ts.html/jayashankarbhupalpally.html/cotton.html')
def tsjbco():
    return render_template('cotton.html')
@app.route('/ts.html/jayashankarbhupalpally.html/groundnut.html')
def tsjbgn():
    return render_template('groundnut.html')





@app.route('/ts.html/warangalurban.html/')
def tswarangalu():
    return render_template('warangalurban.html')

@app.route('/ts.html/warangalurban.html/paddy.html')
def tswarangalupad():
    return render_template('paddy.html')

@app.route('/ts.html/warangalurban.html/maize.html')
def tswarangaluma():
    return render_template('maize.html')
@app.route('/ts.html/warangalurban.html/cotton.html')
def tswarangalucot():
    return render_template('cotton.html')
@app.route('/ts.html/warangalurban.html/groundnut.html')
def tswarangalugn():
    return render_template('groundnut.html')

@app.route('/ts.html/jangaon.html/')
def tsjan():
    return render_template('jangaon.html')
@app.route('/ts.html/jangaon.html/paddy.html')
def tsjanp():
    return render_template('paddy.html')
@app.route('/ts.html/jangaon.html/maize.html')
def tsjanm():
    return render_template('maize.html')

@app.route('/ts.html/jangaon.html/cotton.html')
def tsjanc():
    return render_template('cotton.html')

@app.route('/ts.html/jangaon.html/groundnut.html')
def tsjangn():
    return render_template('groundnut.html')

@app.route('/ts.html/adilabad.html/')
def tsadi():
    return render_template('adilabad.html')
@app.route('/ts.html/adilabad.html/paddy.html')
def tsadipad():
    return render_template('paddy.html')
@app.route('/ts.html/adilabad.html/jowar.html')
def tsadijowa():
    return render_template('jowar.html')
@app.route('/ts.html/adilabad.html/maize.html')
def tsadimaiz():
    return render_template('maize.html')
@app.route('/ts.html/adilabad.html/sunflower.html')
def tsadisun():
    return render_template('sunflower.html')
@app.route('/ts.html/adilabad.html/greengram.html')
def tsadigg():
    return render_template('greengram.html')
@app.route('/ts.html/adilabad.html/bengalgram.html')
def tsadibg():
    return render_template('bengalgram.html')

@app.route('/ts.html/nirmal.html/')
def tsnir():
    return render_template('nirmal.html')
@app.route('/ts.html/nirmal.html/paddy.html')
def tsnirpad():
    return render_template('paddy.html')
@app.route('/ts.html/nirmal.html/jowar.html')
def tsnirjowa():
    return render_template('jowar.html')
@app.route('/ts.html/nirmal.html/maize.html')
def tsnirmaiz():
    return render_template('maize.html')
@app.route('/ts.html/nirmal.html/sunflower.html')
def tsnirsun():
    return render_template('sunflower.html')
@app.route('/ts.html/nirmal.html/greengram.html')
def tsnirgg():
    return render_template('greengram.html')
@app.route('/ts.html/nirmal.html/bengalgram.html')
def tsnirbg():
    return render_template('bengalgram.html')

@app.route('/ts.html/mancherial.html/')
def tsmanc():
    return render_template('mancherial.html')
@app.route('/ts.html/mancherial.html/paddy.html')
def tsmanpad():
    return render_template('paddy.html')
@app.route('/ts.html/mancherial.html/jowar.html')
def tsmancjowa():
    return render_template('jowar.html')
@app.route('/ts.html/mancherial.html/maize.html')
def tsmancmaiz():
    return render_template('maize.html')
@app.route('/ts.html/mancherial.html/sunflower.html')
def tsmancsun():
    return render_template('sunflower.html')
@app.route('/ts.html/mancherial.html/greengram.html')
def tsmancgg():
    return render_template('greengram.html')
@app.route('/ts.html/mancherial.html/bengalgram.html')
def tsmancbg():
    return render_template('bengalgram.html')



@app.route('/ts.html/kumurambheem.html/')
def tskb():
    return render_template('kumurambheem.html')
@app.route('/ts.html/kumurambheem.html/paddy.html')
def tskbpad():
    return render_template('paddy.html')
@app.route('/ts.html/kumurambheem.html/jowar.html')
def tskbjowa():
    return render_template('jowar.html')
@app.route('/ts.html/kumurambheem.html/maize.html')
def tskbmaiz():
    return render_template('maize.html')
@app.route('/ts.html/kumurambheem.html/sunflower.html')
def tskbsun():
    return render_template('sunflower.html')
@app.route('/ts.html/kumurambheem.html/greengram.html')
def tskbgg():
    return render_template('greengram.html')
@app.route('/ts.html/kumurambheem.html/bengalgram.html')
def tskbbg():
    return render_template('bengalgram.html')

@app.route('/ts.html/karimnagar.html/')
def tskan():
    return render_template('karimnagar.html')

@app.route('/ts.html/karimnagar.html/paddy.html')
def tskanpad():
    return render_template('paddy.html')
@app.route('/ts.html/karimnagar.html/maize.html')
def tskanmai():
    return render_template('maize.html')
@app.route('/ts.html/karimnagar.html/cotton.html')
def tskancot():
    return render_template('cotton.html')
@app.route('/ts.html/karimnagar.html/chilli.html')
def tskanchil():
    return render_template('chilli.html')

@app.route('/ts.html/karimnagar.html/turmeric.html')
def tskantur():
    return render_template('turmeric.html')

@app.route('/ts.html/jagtial.html/')
def tsjag():
    return render_template('jagtial.html')
@app.route('/ts.html/jagtial.html/paddy.html')
def tsjagpad():
    return render_template('paddy.html')
@app.route('/ts.html/jagtial.html/maize.html')
def tsjagmai():
    return render_template('maize.html')
@app.route('/ts.html/jagtial.html/cotton.html')
def tsjagcot():
    return render_template('cotton.html')
@app.route('/ts.html/jagtial.html/chilli.html')
def tsjagchil():
    return render_template('chilli.html')

@app.route('/ts.html/jagtial.html/turmeric.html')
def tsjagtur():
    return render_template('turmeric.html')

@app.route('/ts.html/rajannasircilla.html/')
def tsrs():
    return render_template('rajannasircilla.html')
@app.route('/ts.html/rajannasircilla.html/paddy.html')
def tsrspad():
    return render_template('paddy.html')
@app.route('/ts.html/rajannasircilla.html/maize.html')
def tsrsmai():
    return render_template('maize.html')
@app.route('/ts.html/rajannasircilla.html/cotton.html')
def tsrscot():
    return render_template('cotton.html')
@app.route('/ts.html/rajannasircilla.html/chilli.html')
def tsrschil():
    return render_template('chilli.html')

@app.route('/ts.html/rajannasircilla.html/turmeric.html')
def tsrstur():
    return render_template('turmeric.html')


@app.route('/ts.html/peddapalli.html/')
def tspp():
    return render_template('peddapalli.html')
@app.route('/ts.html/peddapalli.html/paddy.html')
def tspppad():
    return render_template('paddy.html')
@app.route('/ts.html/peddapalli.html/maize.html')
def tsppmai():
    return render_template('maize.html')
@app.route('/ts.html/peddapalli.html/cotton.html')
def tsppcot():
    return render_template('cotton.html')
@app.route('/ts.html/peddapalli.html/chilli.html')
def tsppchil():
    return render_template('chilli.html')

@app.route('/ts.html/peddapalli.html/turmeric.html')
def tspptur():
    return render_template('turmeric.html')


@app.route('/ts.html/khammam.html/')
def tskham():
    return render_template('khammam.html')

@app.route('/ts.html/khammam.html/paddy.html')
def tskhampad():
    return render_template('paddy.html')

@app.route('/ts.html/khammam.html/cotton.html')
def tskhamcot():
    return render_template('cotton.html')

@app.route('/ts.html/khammam.html/greengram.html')
def tskhamgg():
    return render_template('greengram.html')

@app.route('/ts.html/bhadradrikothagudem.html/')
def tsbk():
    return render_template('bhadradrikothagudem.html')

@app.route('/ts.html/bhadradrikothagudem.html/paddy.html')
def tsbkpad():
    return render_template('paddy.html')

@app.route('/ts.html/bhadradrikothagudem.html/cotton.html')
def tsbkcot():
    return render_template('cotton.html')

@app.route('/ts.html/bhadradrikothagudem.html/greengram.html')
def tsbkgg():
    return render_template('greengram.html')


@app.route('/ts.html/nalgonda.html/')
def tsnal():
    return render_template('nalgonda.html')

@app.route('/ts.html/nalgonda.html/paddy.html')
def tsnalpad():
    return render_template('paddy.html')
@app.route('/ts.html/nalgonda.html/jowar.html')
def tsnaljow():
    return render_template('jowar.html')
@app.route('/ts.html/nalgonda.html/bajra.html')
def tsnalbaj():
    return render_template('bajra.html')

@app.route('/ts.html/nalgonda.html/groundnut.html')
def tsnalgn():
    return render_template('groundnut.html')
@app.route('/ts.html/nalgonda.html/cotton.html')
def tsnalcot():
    return render_template('cotton.html')


@app.route('/ts.html/suryapet.html/')
def tssur():
    return render_template('suryapet.html')

@app.route('/ts.html/suryapet.html/paddy.html')
def tssppad():
    return render_template('paddy.html')
@app.route('/ts.html/suryapet.html/jowar.html')
def tsspjow():
    return render_template('jowar.html')
@app.route('/ts.html/suryapet.html/bajra.html')
def tsspbaj():
    return render_template('bajra.html')

@app.route('/ts.html/suryapet.html/groundnut.html')
def tsspgn():
    return render_template('groundnut.html')
@app.route('/ts.html/suryapet.html/cotton.html')
def tsspcot():
    return render_template('cotton.html')


@app.route('/ts.html/yadadribhuvanagiri.html/')
def tsyb():
    return render_template('yadadribhuvanagiri.html')

@app.route('/ts.html/yadadribhuvanagiri.html/paddy.html')
def tsybpad():
    return render_template('paddy.html')
@app.route('/ts.html/yadadribhuvanagiri.html/jowar.html')
def tsybjow():
    return render_template('jowar.html')
@app.route('/ts.html/yadadribhuvanagiri.html/bajra.html')
def tsybbaj():
    return render_template('bajra.html')

@app.route('/ts.html/yadadribhuvanagiri.html/groundnut.html')
def tsybgn():
    return render_template('groundnut.html')
@app.route('/ts.html/yadadribhuvanagiri.html/cotton.html')
def tsybcot():
    return render_template('cotton.html')


@app.route('/ts.html/nizambad.html/')
def tsni():
    return render_template('nizambad.html')

@app.route('/ts.html/nizambad.html/paddy.html')
def tsnipad():
    return render_template('paddy.html')

@app.route('/ts.html/nizambad.html/sugarcane.html')
def tsnisc():
    return render_template('sugarcane.html')
@app.route('/ts.html/nizambad.html/maize.html')
def tsnimai():
    return render_template('maize.html')
@app.route('/ts.html/nizambad.html/turmeric.html')
def tsnitur():
    return render_template('turmeric.html')
@app.route('/ts.html/nizambad.html/cotton.html')
def tsnicot():
    return render_template('cotton.html')
@app.route('/ts.html/nizambad.html/groundnut.html')
def tsnign():
    return render_template('groundnut.html')
@app.route('/ts.html/nizambad.html/sunflower.html')
def tsnisf():
    return render_template('sunflower.html')




@app.route('/ts.html/kamareddy.html/')
def tskmr():
    return render_template('kamareddy.html')

@app.route('/ts.html/kamareddy.html/paddy.html')
def tskmrpad():
    return render_template('paddy.html')

@app.route('/ts.html/kamareddy.html/sugarcane.html')
def tskmrsc():
    return render_template('sugarcane.html')
@app.route('/ts.html/kamareddy.html/maize.html')
def tskmrmai():
    return render_template('maize.html')
@app.route('/ts.html/kamareddy.html/turmeric.html')
def tskmrtur():
    return render_template('turmeric.html')
@app.route('/ts.html/kamareddy.html/cotton.html')
def tskmrcot():
    return render_template('cotton.html')
@app.route('/ts.html/kamareddy.html/groundnut.html')
def tskmrgn():
    return render_template('groundnut.html')
@app.route('/ts.html/kamareddy.html/sunflower.html')
def tskmrsf():
    return render_template('sunflower.html')



@app.route('/ts.html/medak.html/')
def tsmed():
    return render_template('medak.html')

@app.route('/ts.html/medak.html/paddy.html')
def tsmedpad():
    return render_template('paddy.html')

@app.route('/ts.html/medak.html/sugarcane.html')
def tsmedsc():
    return render_template('sugarcane.html')
@app.route('/ts.html/medak.html/maize.html')
def tsmedmai():
    return render_template('maize.html')
@app.route('/ts.html/medak.html/ragi.html')
def tsmedragi():
    return render_template('ragi.html')

@app.route('/ts.html/siddipet.html/')
def tssid():
    return render_template('siddipet.html')

@app.route('/ts.html/siddipet.html/paddy.html')
def tssidpad():
    return render_template('paddy.html')

@app.route('/ts.html/siddipet.html/sugarcane.html')
def tssidsc():
    return render_template('sugarcane.html')
@app.route('/ts.html/siddipet.html/maize.html')
def tssidmai():
    return render_template('maize.html')
@app.route('/ts.html/siddipet.html/ragi.html')
def tssidragi():
    return render_template('ragi.html')


@app.route('/ts.html/sangareddy.html/')
def tssang():
    return render_template('sangareddy.html')

@app.route('/ts.html/sangareddy.html/paddy.html')
def tssangpad():
    return render_template('paddy.html')

@app.route('/ts.html/sangareddy.html/sugarcane.html')
def tssangsc():
    return render_template('sugarcane.html')
@app.route('/ts.html/sangareddy.html/maize.html')
def tssangmai():
    return render_template('maize.html')
@app.route('/ts.html/sangareddy.html/ragi.html')
def tssangragi():
    return render_template('ragi.html')

@app.route('/ts.html/rangareddy.html/')
def tsrang():
    return render_template('rangareddy.html')

@app.route('/ts.html/rangareddy.html/cotton.html')
def tsrangcot():
    return render_template('cotton.html')
@app.route('/ts.html/rangareddy.html/maize.html')
def tsrangmai():
    return render_template('maize.html')
@app.route('/ts.html/rangareddy.html/red gram.html')
def tsrangrg():
    return render_template('red gram.html')
@app.route('/ts.html/rangareddy.html/paddy.html')
def tsrangpad():
    return render_template('paddy.html')
@app.route('/ts.html/rangareddy.html/jowar.html')
def tsrangjow():
    return render_template('jowar.html')
@app.route('/ts.html/rangareddy.html/greengram.html')
def tsranggg():
    return render_template('greengram.html')


@app.route('/ts.html/medchal.html/')
def tsmedc():
    return render_template('medchal.html')

@app.route('/ts.html/medchal.html/cotton.html')
def tsmedccot():
    return render_template('cotton.html')
@app.route('/ts.html/medchal.html/maize.html')
def tsmedcmai():
    return render_template('maize.html')
@app.route('/ts.html/medchal.html/red gram.html')
def tsmedcrg():
    return render_template('red gram.html')
@app.route('/ts.html/medchal.html/paddy.html')
def tsmedcpad():
    return render_template('paddy.html')
@app.route('/ts.html/medchal.html/jowar.html')
def tsmedcjow():
    return render_template('jowar.html')
@app.route('/ts.html/medchal.html/greengram.html')
def tsmedcgg():
    return render_template('greengram.html')
@app.route('/ts.html/hyderabad.html/')
def tshyd():
    return render_template('hyderabad.html')


@app.route('/ts.html/vikarabad.html/')
def tsvikc():
    return render_template('vikarabad.html')

@app.route('/ts.html/vikarabad.html/cotton.html')
def tsvikcot():
    return render_template('cotton.html')
@app.route('/ts.html/vikarabad.html/maize.html')
def tsvikmai():
    return render_template('maize.html')
@app.route('/ts.html/vikarabad.html/red gram.html')
def tsvikrg():
    return render_template('red gram.html')
@app.route('/ts.html/vikarabad.html/paddy.html')
def tsvikpad():
    return render_template('paddy.html')
@app.route('/ts.html/vikarabad.html/jowar.html')
def tsvikjow():
    return render_template('jowar.html')
@app.route('/ts.html/vikarabad.html/greengram.html')
def tsvikgg():
    return render_template('greengram.html')

@app.route('/ts.html/mahboobnagar.html/')
def tsmahboobnagar():
    return render_template('mahboobnagar.html')
@app.route('/ts.html/mahboobnagar.html/maize.html')
def tsmahboobnagarmai():
    return render_template('maize.html')
@app.route('/ts.html/mahboobnagar.html/paddy.html')
def tsmahboobnagarpad():
    return render_template('paddy.html')
@app.route('/ts.html/mahboobnagar.html/greengram.html')
def tsmahboobnagargg():
    return render_template('greengram.html')

@app.route('/ts.html/jogulambagadwal.html/')
def tsjg():
    return render_template('jogulambagadwal.html')
@app.route('/ts.html/jogulambagadwal.html/maize.html')
def tsjbmai():
    return render_template('maize.html')
@app.route('/ts.html/jogulambagadwal.html/paddy.html')
def tsjbpad():
    return render_template('paddy.html')
@app.route('/ts.html/jogulambagadwal.html/greengram.html')
def tsjbgg():
    return render_template('greengram.html')

@app.route('/ts.html/nagarkurnool.html/')
def tsnk():
    return render_template('nagarkurnool.html')
@app.route('/ts.html/nagarkurnool.html/maize.html')
def tsnkmai():
    return render_template('maize.html')
@app.route('/ts.html/nagarkurnool.html/paddy.html')
def tsnkpad():
    return render_template('paddy.html')
@app.route('/ts.html/nagarkurnool.html/greengram.html')
def tsnkgg():
    return render_template('greengram.html')



@app.route('/ts.html/wanaparthy.html/')
def tswp():
    return render_template('wanaparthy.html')
@app.route('/ts.html/wanaparthy.html/maize.html')
def tswpmai():
    return render_template('maize.html')
@app.route('/ts.html/wanaparthy.html/paddy.html')
def tswppad():
    return render_template('paddy.html')
@app.route('/ts.html/wanaparthy.html/greengram.html')
def tswpgg():
    return render_template('greengram.html')














if __name__ == '__main__':
    socketio.run(app, debug=True)

