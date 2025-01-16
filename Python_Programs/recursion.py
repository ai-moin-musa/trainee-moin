
def find_file(dir,filename,path=''):
	for key,value in dir.items():
		
		curr_path = f"{path}\\{key}"
		
		if key == filename:
			return curr_path
			
		if isinstance(value,dict):
			result = find_file(value,filename,curr_path)
			if result is not None:
				return result
		
		

main_dir={
	'documents': {
		'work':{'report.docx': None, 'file.exe': None},
		'personal':{'vacation.png': None, 'birthday.png':None}
	},
	'downloads':{'this.png':None},
	'songs':{
		'myfav':{'fav1.mp4':None,'fav2.mp4':None},
		'alltimefav':{'alfav1.mp4':None,'alfav2.mp4':None}
	}
}


filename = str(input("Enter filename: "))

path = (find_file(main_dir,filename))

if path is None:
	print("file does not exits")
else:
	print(f"file {filename} found at {path}")
