## Error Code Lookup Table -- Rorze R716 Robot


## 1. Identification codes of the controlllers

Id_code_table = {'01':'X-axis', '02':'Z-axis', '03':'Rotation', '04':'Upper arm', '05':'Lower arm',
				 '06':'Encoder Master', '80':'Rotation + Upper Arm + Lower Arm', 
				 '81':'Rotation + Upper arm', '82':'Rotation + Lower Arm', 
				 '90':'Z-axis + Rotation + Both arms', '91':'Z-axis + Rotation + Upper arm',
				 '92':'Z-axis + Rotation + Lower arm', '95':'Z-axis + Rotation', 
				 '96':'Upper arm + Lower arm', '7F':'RC-400', 'FF':'SYSTEM'}

## 2. Error Coedes (except FF)

Error_Code_WtFF = {'20':'Checksum error of data received from RS-232C port', 
				   '21':'Checksum error of data received from RS-485 port', '22':'Command error',
				   '23':'Command Error', '24':'Command Error', '25':'Command Error', '26':'Command Error',
				   '27':'Virtual Body No. that is not set is used', '28':'Impropercommand target Body No.',
				   '29':'Command transmited to RS-485 port is not reveived properly',
				   '2A':'Command transmited to RS-485 port is canceled',
				   '2B':'Communication time-out of the command transmitted to RS-485 port has occurred',
				   '2C':'Transmitted target of command transmitted to RS-485 port is not RC-400',
				   '2D':'Communication speed designated by command parameter is not proper',
				   '2E':'Changing the communication speed of RS-485 lines for all controllers connected has not complted properly.',
				   '2F':'Controller is not connected to RS-485 port',
				   '30':'Polling stop command is executed before starting polling', '40':'Start-up speed (OL) not set',
				   '41':'Max. speed (OH) not set', '42':'Maximum acceleration speed (OS) not set',
				   '42':'Maximum acceleration speed (OS) not set',
				   '43':'Acceleration increasing interval ratio (OA) not set',
				   '44':'Acceleration decreasing interval ratio (OB) not set',
				   '45':'Start-up speed (OL) is greater than max. speed (OH)',
				   '46':'(OA) + (OB) > 100', '47':'Acceleration/decleration pattern not set',
				   '48':'Hardware malfunction', '49':'improper command code', '4A':'Improper command parameter',
				   '4B'：'Checksum error of the command received from RC-400',
				   '4C':'Same group command is executed while a command is executing.',
				   '83':'ORG search not allowed', '84':'VAC ON error', '06':'VAC OFF error'
				   }

				   
Error_Code_FF = {'10': 'Operation time-out', '11': 'Communication Time out', 
				 '12': 'Encoder battery error(Battery must be replaced)',
				 '13': 'Absolute encoder data lost',
				 'FF': 'Abnornmal program or abnormail communication format'}

