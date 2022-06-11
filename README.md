# threadedTransfer
Made for cronjobs with IO intensive file transfers. Allows for easy threaded file transfers from multiple remote and local file directories at once.

## Parameters:
  ### -i, --input: Sets the input file location, Input can be delimitered with a comma to include multiple sources.
  
  Eg: ./main.py -i /home/user/,user@server:/home/user/ -o user@server:/media/user/backupDisk/backup
  
  Backs up /home/user/ and user@server:/home/user/ into a folder named 'backup' in user@server:/media/user/backupDisk/
  
  ### -o, --output: Sets the output file location and copies file from the input location into a folder.
  
  Eg: ./main.py -i /home/user/Pictures -o /media/user/backupDisk/Pictures
  
  ### -a, --archive: Archives output into a .zip file instead of a folder.
  
  Eg: ./main.py -i /home/user/Pictures -oa /media/user/backupDisk/Pictures
  
  Outputs a zip file in /media/user/backupDisk/ called 'Pictures.zip'
  
  ### -d, --date: appends a datetime to the end of your output file name in the format of %m-%d-%Y_%H%M%S (month-date-year_HrMinSec)
  
  Eg: ./main.py -i /home/user/Pictures -oad /media/user/backupDisk/Pictures-
  
  Outputs a zip file in /media/user/backupDisk called 'Pictures-06-10-2022_123000.zip'

