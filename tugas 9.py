
print('\n')
biodata = { 'nama'  : 'Muh Ariel',
'nim'   : '231031099',
'kelas' : 'S123D',
'tempat,tanggal lahir' : 'rappang,13 februari2003',
'jenis kelamin' : 'laki-laki',
'agama' : 'islam',
'alamat': 'jalan sultan hasanuddin no.88',
'email' : 'muhariel7104@gmail.com'
}

print(biodata.keys())
print(biodata.values())

print()
selected_biodata = dict(list(biodata.items())[:6])
print(selected_biodata)





