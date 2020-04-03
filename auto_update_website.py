try:
    import time
    time.sleep(10)
    password='!Duck12345'
    username='maruffolo'
    
    top_html='''
        <style>
    /*  https://codepen.io/team/css-tricks/pen/wXgJww?editors=1100
    	Max width before this PARTICULAR table gets nasty. This query will take effect for any screen smaller than 760px and also iPads specifically.
    	*/
    	@media
    	  only screen 
        and (max-width: 760px), (min-device-width: 768px) 
        and (max-device-width: 1024px)  {
    
    		/* Force table to not be like tables anymore */
    		table, thead, tbody, th, td, tr {
    			display: block;
    		}
    
    		/* Hide table headers (but not display: none;, for accessibility) */
    		thead tr {
    			position: absolute;
    			top: -9999px;
    			left: -9999px;
    		}
    
        tr {
          margin: 0 0 1rem 0;
        }
          
        tr:nth-child(odd) {
          background: #2a2a2a;
        }
        
    		td {
    			/* Behave  like a "row" */
    			border: none;
    			border-bottom: 1px solid #eee;
    			position: relative;
    			padding-left: 0%;
    		}
    
    		td:before {
    			/* Now like a table header */
    			position: absolute;
    			/* Top/left values mimic padding */
    			top: 0;
    			left: 6px;
    			width: 45%;
    			padding-right: 10px;
    			white-space: nowrap;
    		}
    
    		/*
    		Label the data
        You could also use a data-* attribute and content for this. That way "bloats" the HTML, this way means you need to keep HTML and CSS in sync. Lea Verou has a clever way to handle with text-shadow.
    		*/
    		td:nth-of-type(1):before { content: ""; }
    		td:nth-of-type(2):before { content: ""; }
    	}
        </style>
    
    <!DOCTYPE HTML>
    <html>
    
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="user-scalable=no, width=device-width" />
        <title>Live Updating Website</title>
    
    
    <script type="text/javascript">
    window.onload = function () {
    
    var chart = new CanvasJS.Chart("chartContainer", {
    	theme: "dark1", // "light2", "dark1", "dark2"
    	animationEnabled: false, // change to true		
    	title:{
    		text: "@slay_the_normies Live Updating 4H Ethereum Chart"
    	},
    	data: [
    	{
    		// Change type to "bar", "area", "spline", "pie",etc.
    		type: "area",
    		dataPoints: [
    '''
    bot_html='''
    		]
    	}
    	]
    });
    chart.render();
    
    }
    </script>
    </head>
    <body style="background-color:#2a2a2a;"><center>
    <div id="chartContainer" style="height: 370px; width: 100%;"></div>
    <script src="https://canvasjs.com/assets/script/canvasjs.min.js"> </script>
    <h1><font color="white">Live Python Console Output</font></h3>
    <table role="table">
      <thead role="rowgroup">
        <tr role="row">
     
      </thead>
      <tbody role="rowgroup">
        <tr role="row">
          <td role="cell"><p style="text-align: center;"><font color="white">
    '''
    end_html=''' 
          </font></p></td>
          <td role="cell"><center>
          <img style="display:block;" width="100%" height="100%" src="https://steamuserimages-a.akamaihd.net/ugc/941686516770115673/44CD9D845B222B3B1179C15A0DF2DBBF287643A7/" />
          </center></td>
    
        </tr>
    
      </tbody>
    </table>
    </center>
    </body>
    </html>
    '''
    from prettytable import PrettyTable
    import datetime
    from bs4 import BeautifulSoup
    import requests
    response = requests.get('https://api.kraken.com/0/public/OHLC?pair=ETHUSD&interval=240')
    html = response.content
    soup = BeautifulSoup(html, "html.parser")
    eth_string=str(soup)
    #print(len(eth_string))
    eth_string=eth_string[53880:]
    find_start=eth_string.find("]")
    end_trim=eth_string.find('],"')
    eth_string=eth_string[find_start+2:end_trim]
    s=eth_string.count("]")
    e_counter=eth_string.count("[")
    x = PrettyTable()
    x.field_names = [" ", "  "]
    #print(s)
    while (e_counter >=1):
        if e_counter>1:
            end=","
        else:
            end=""
        find_start=eth_string.find("[")
        find_end=eth_string.find("]")
        candle=eth_string[find_start:find_end]
        #print(e_counter,candle)
        time=candle[1:11]
        price=float(candle[49:55])
        price=round(price,2)
        time=datetime.datetime.fromtimestamp(int(time)).strftime('%Y-%m-%d %I:%M:%p')
        #time=time[:]
        time=time.replace("-","/")
    
        '''
        if '00' in time[5:9] or '01' in time[5:9] or '02' in time[5:9] or '03' in time[5:9] or '04' in time[5:9] or '05' in time[5:9] or '06' in time[5:9] or'07' in time[5:9] or '08' in time[5:9] or '09' in time[5:9]:
            time=time.replace("0","")
        time=time+" O'clock"
        if "  " in time:
            time=time[0:4]+" 0 O"+time[7:]
        time=time.replace("-","/")
        '''
        x.add_row(['{ label: "'+time+'" ,', 'y: '+str(price)+' } '+end])
        #{ label: "1",  y: 10  }
        #print(time[5:10],price)
        eth_string=eth_string[find_end+1:]
        e_counter=e_counter-1
    x=str(x)
    from pathlib import Path
    path = str(Path(__file__).parent.absolute())
    path1=path.replace("\\","\\\\")
    
    from os import path
    order_statetxt = open(path1+'/outputfile2.txt', 'r')
    order_state = str(order_statetxt.readlines())
    order_state=order_state.replace("\\n","\n<br>")
    order_state=order_state[1:-1]
    order_state=order_state.replace("'","")
    order_state=order_state.replace(",","")
    order_state=order_state.replace('"',"")
    order_state=order_state.replace('============================================','\n<br>')
    order_state=order_state.replace('=',"")
    #print(order_state)
    import datetime
    if 'done' in order_state:
        
        order_state=order_state[order_state.find('done'):]
        order_state=order_state.replace('done','Python Console Timestamp: \n<br>'+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'\n<br><br>')
        order_state=order_state.replace('age','age <font color="#2a2a2a"> oooo</font>')
    else:
        order_state=order_state.replace("<br>","<br><br>")
        order_state=order_state.replace("</font><br><br><br>","<br>")
        order_state=order_state[order_state.find('ESS')+4:]
        order_state='Python Console Timestamp: \n<br>'+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'\n<br><br> Trade Currently Open <font color="#2a2a2a"> @@@@@@@@@@@@@@@@@</font><br>'+order_state
    x=x.replace("+","")
    x=x.replace("|","")
    x=x.replace("-","")
    final=top_html+x+bot_html+order_state+end_html
    final=final.replace("</font><br><br><br>","</font><br>")
    #print("done")
    print(final, file=open(path1+"/web.html", "w"))
    #print(final)
    
    import paramiko
    from scp import SCPClient
    
    def createSSHClient(server, port, user, password):
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(server, port, user, password)
        return client
    
    ssh = createSSHClient('matrix.senecacollege.ca', '22', username, password)
    scp = SCPClient(ssh.get_transport())
    
    scp.put(path1+'/web.html', recursive=True, remote_path='~/public_html/eth.html')
    
    scp.close()
    
    print('done',str(datetime.datetime.now()))
    
except Exception as e:#always have exceptions while scripts loop for long periods of time. Script can crash if internet connection is lost without exceptions.
     print(str(e))   
