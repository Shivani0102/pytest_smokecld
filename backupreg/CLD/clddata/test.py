from testrail import *

client = APIClient('https://dev.azure.com/Blights/CAS%20Testing/_testManagement/')
client.user = 'ashish.rawat@berkeleylights.com'
client.password = '#Lights2019@'

name = "Testing"
# test_case_ids = [222466, 222468, 222469, 222470, 222471, 222475, 222476, 222480, 222481, 222482, 222483, 222485, 222486,
#                  222488, 222489, 222490, 222491, 222492, 222493, 222494, 222498, 222499, 222500, 222502, 222507, 222508,
#                  222511, 222513, 222514, 222515, 222523, 222531, 222532, 222538, 222540, 222543, 222544, 222545, 222546,
#                  222547, 222548, 222549, 222550, 222551, 222552, 222553, 222556, 222558, 222560, 222562, 222564, 222568,
#                  222569, 222570, 222571, 239898, 239900, 239903, 239905, 239907, 239912, 239913, 239914, 239915, 239916,
#                  239917, 239921, 239922, 239925, 239926, 239927, 239928, 239929, 239930, 239932, 239937, 239940, 239941,
#                  239931, 222622, 222623,
#                  222624, 222625, 222626, 222631, 222633, 222636, 222637, 222638, 222643, 222642, 222644, 222645, 222647,
#                  222648,
#                  222651, 222652,
#                  222653, 222656, 222657, 222659, 222661, 222666, 222668, 222667, 222669, 222670, 222671, 222672, 222673,
#                  222674, 222676, 222677, 222679, 222680, 222681, 222682, 222683, 222684, 222685, 222686, 222687, 222688,
#                  222689,
#                  222690,
#                  222691, 222693, 222694, 222695, 222696, 222697, 222698, 222699, 222700, 222703]

test_case_ids=[30813]
response = client.send_post(
    'add_run/2',
    {'name': name,
     # 'include_all': False,
     # 'case_ids': test_case_ids
     }
)
print(response)
run_id = str(response["id"])
print(run_id)