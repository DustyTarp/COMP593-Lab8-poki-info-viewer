from tkinter import *
from tkinter import ttk
from pokiapi import get_poki_info


def main():

    root = Tk()
    root.title("Pokemon Info Viewer")
    root.iconbitmap("pika.ico")
    root.resizable(False, False)

    frm_user_input = ttk.Frame(root)
    frm_user_input.grid(row=0, column=0, columnspan=2, padx=10, pady=10)


    frm_poki_info = ttk.LabelFrame(root, text='Info')
    frm_poki_info.grid(row=1, column=0, padx=10, pady=10, sticky=N)

    frm_poki_stats = ttk.LabelFrame(root, text='Stats')
    frm_poki_stats.grid(row=1, column=1, padx=10, pady=10, sticky=N)

    #populate top frame
    lbl_name = ttk.Label(frm_user_input, text="Pokemon Name: ")
    lbl_name.grid(row=0, column=0, padx=10, pady=10)

    ent_name = ttk.Entry(frm_user_input)
    ent_name.grid(row=0, column=1, pady=10)

    def btn_get_info_click():
        #Get pokemon info from pokiapi
        pokemon_name = ent_name.get()
        poki_dict = get_poki_info(pokemon_name)

        #populate displayed pokemon values
        if poki_dict:
            lbl_height_value['text'] = str(poki_dict['height']) + ' dm'
            lbl_weight_value['text'] = str(poki_dict['weight']) + ' hg'

            types_list = [t['type']['name'] for t in poki_dict['types']]
            lbl_type_value['text'] = ', '.join(types_list)
            prg_hp['value'] = poki_dict['stats'][0]['base_stat']
            prg_att['value'] = poki_dict['stats'][1]['base_stat']
            prg_def['value'] = poki_dict['stats'][2]['base_stat']
            prg_sp_attack['value'] = poki_dict['stats'][3]['base_stat']
            prg_sp_defense['value'] = poki_dict['stats'][4]['base_stat']
            prg_speed['value'] = poki_dict['stats'][5]['base_stat']

        

    btn_get_info = ttk.Button(frm_user_input, text="Get Info", command=btn_get_info_click)
    btn_get_info.grid(row=0, column=2, padx=10, pady=10)

    #populate the info widgets
    lbl_height = ttk.Label(frm_poki_info, text='Height: ')
    lbl_height.grid(row=100, column=100, padx=(10,0), pady=10, sticky=E)

    lbl_height_value = ttk.Label(frm_poki_info)
    lbl_height_value.grid(row=100, column=200, padx=(2,10), pady=10, sticky=W)

    lbl_weight = ttk.Label(frm_poki_info, text='Weight: ')
    lbl_weight.grid(row=200, column=100, padx=(10,0), pady=10, sticky=E)

    lbl_weight_value = ttk.Label(frm_poki_info)
    lbl_weight_value.grid(row=200, column=200, padx=(2,10), pady=10, sticky=W)

    lbl_type = ttk.Label(frm_poki_info, text='Type: ')
    lbl_type.grid(row=300, column=100, padx=(10,0), pady=10, sticky=E)

    lbl_type_value = ttk.Label(frm_poki_info, width=20)
    lbl_type_value.grid(row=300, column=200, padx=(2,10), pady=10, sticky=W)

    #populate the stats widgets
    lbl_hp = ttk.Label(frm_poki_stats, text='HP: ')
    lbl_hp.grid(row=100, column=100, padx=(10,0), pady=10, sticky=E)
    prg_hp = ttk.Progressbar(frm_poki_stats, length=200, maximum=255)
    prg_hp.grid(row=100, column=200, padx=(2,10), pady=10, sticky=W)

    lbl_attack = ttk.Label(frm_poki_stats, text='Attack: ')
    lbl_attack.grid(row=200, column=100, padx=(10,0), pady=10, sticky=E)
    prg_att = ttk.Progressbar(frm_poki_stats, length=200, maximum=255)
    prg_att.grid(row=200, column=200, padx=(2,10), pady=10, sticky=W)

    lbl_defense = ttk.Label(frm_poki_stats, text='Defense: ')
    lbl_defense.grid(row=300, column=100, padx=(10,0), pady=10, sticky=E)
    prg_def = ttk.Progressbar(frm_poki_stats, length=200, maximum=255)
    prg_def.grid(row=300, column=200, padx=(2,10), pady=10, sticky=W)

    lbl_sp_attack = ttk.Label(frm_poki_stats, text='Special Attack: ')
    lbl_sp_attack.grid(row=400, column=100, padx=(10,0), pady=10, sticky=E)
    prg_sp_attack = ttk.Progressbar(frm_poki_stats, length=200, maximum=255)
    prg_sp_attack.grid(row=400, column=200, padx=(2,10), pady=10, sticky=W)

    lbl_sp_defense = ttk.Label(frm_poki_stats, text='Special Defense: ')
    lbl_sp_defense.grid(row=500, column=100, padx=(10,0), pady=10, sticky=E)
    prg_sp_defense = ttk.Progressbar(frm_poki_stats, length=200, maximum=255)
    prg_sp_defense.grid(row=500, column=200, padx=(2,10), pady=10, sticky=W)

    lbl_speed = ttk.Label(frm_poki_stats, text='Speed: ')
    lbl_speed.grid(row=600, column=100, padx=(10,0), pady=10, sticky=E)
    prg_speed = ttk.Progressbar(frm_poki_stats, length=200, maximum=255)
    prg_speed.grid(row=600, column=200,padx=(2,10), pady=10, sticky=W)


    root.mainloop()

main()