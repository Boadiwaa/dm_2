# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 14:45:19 2023

@author: pauli
"""
#TYPE 2 DM ALGORITHM

#DRUGS TO BE USED WITH CAUTION ENCLOSED IN ASTERIX

# QUESTIONS:

    # ENTER CLIENT'S BMI:
        # IF BMI ≥25 CHOOSE SEVERITY OF COMPLICATIONS: (INCLUDE EXAMPLES TO AID PHYSICIANS)
            #NONE - LIFESTYLE THERAPY
            #MILD TO MODERATE OR (BMI ≥27):-  ABOVE + MEDICAL THERAPY - select one of the following based on efficacy, safety,
                                                # and patients’ clinical profile: phentermine, orlistat, lorcaserin,
                                                # phentermine/topiramate ER, naltrexone/bupropion, liraglutide 3 mg
            #SEVERE OR (BMI ≥35): - ABOVE + SURGICAL THERAPY -  Endoscopic procedures, gastric banding, sleeve, or bypass
    #PRE-DM CRITERIA (3)
    #ENTER CLIENT'S FASTING GLUCOSE: IFG is defined as fasting plasma glucose values of 100 to 125 mg per dL (5.6 to 6.9 mmol per L) 
    #>= 7 = DM
    #ENTER CLIENT'S 2-HOUR POST-PRANDIAL GLUCOSE:  Impaired glucose tolerance is defined as two-hour glucose levels of 140 to 199 mg per dL (7.8 to 11.0 mmol)
    #>11 = DM
    
    #IS THERE METABOLIC SYNDROME PRESENT? According to the NCEP ATP III definition, metabolic syndrome is present 
        #if three or more of the following five criteria are met: waist circumference over 40 inches (men) or 35 inches (women),
        #blood pressure over 130/85 mmHg, fasting triglyceride (TG) level over 150 mg/dl, 
        #fasting high-density lipoprotein (HDL) cholesterol level less than 40 mg/dl (men) or 50 mg/dl (women) and fasting blood sugar over 100 mg/dl.
        
    # IF 1 PRE-DM - Metformin, Acarbose
    # IF MORE THAN 2 PRE-DM - in addition, consider: TZD , GLP-1RA
    
    # DM (DRUGS ARE IN ORDER OF HIERARCHY)
    #if established  ASCVD or high risk, CKD 3, or HFrEF - LONG-ACTING glp1-RA OR SGLT2i EG.: FOR CKD 3: canagliflozin; HFrEF: dapagliflozin
    #CURRENT DM MEDS: CHOOSE FROM LIST If not at goal in 3 months, proceed to next level therapy
    #DURATION OF THERAPY SINCE CURRENT MEDS WERE INITIATED
    #ENTER ENTRY HBAIC: PERSONALIZE ACCORDING TO TARGET HBA1C BASED ON CONCURRENT ILLNESS AND RISK OF HYPOGLYCEMIA
        #<7.5% - MONOTHERAPY, E.G. Metformin, GLP1-RA ,SGLT2i, DPP4i,*TZD*, AGi, *SU/GLN*
        #7.5% - 9% DUAL THERAPY, METFORMIN + E.G. GLP1-RA ,SGLT2i, DPP4i,*TZD*,*SU/GLN*, *Basal insulin*, Colesevelam,Bromocriptine QR, AGi
        #  AND IF NO IMPROVEMENT BY 3 MONTHS: TRIPLE THERAPY: METFORMIN + E.G. GLP1-RA ,SGLT2i,*TZD*,*SU/GLN*, *Basal insulin*, DPP4i,Colesevelam,Bromocriptine QR, AGi
        # > 9.0%: 
            #NO SYMPTOMS: DUAL OR TRIPLE THERAPY
            # HAS SYMPTOMS: INSULIN +/- OTHER AGENTS. ADD OR INTENSIFY SYMPTOMS IF NO IMPROVEMENT PER INSULIN ALGORITHM
            
    #ADD DOSAGES OF THE DRUGS USING UPTODATE REFERENCES
    
import flet as ft

# a = ft.TextField(label="Enter BMI (kg/squared metres)",
#           helper_text=""" Round to one decimal place. 
#           Example: 25.5
#           """, 
#          max_length=4,keyboard_type = ft.KeyboardType.NUMBER,
#          icon=ft.icons.PERSON)
# bmi = ft.Row(controls=[a]#alignment=ft.MainAxisAlignment.CENTER)
# )

bc = "#034c81"
ic ="#fffff0"
appbar = ft.AppBar(
  leading=ft.Row([ft.IconButton(ft.icons.INFO, icon_size = 50, icon_color=ic), ft.IconButton(
      ft.icons.SCIENCE, icon_size = 50, icon_color=ic)]
      ), 
  leading_width=100,
title=ft.Text("Type II Diabetes Mellitus Algorithm - Medication Recommendations for Adults",size=30, text_align="start", color = "#fffff0"),#"Segoe Print"
center_title=True,
toolbar_height=80,
   bgcolor=bc,
   actions=[ft.IconButton(ft.icons.SCIENCE, icon_size = 50, icon_color=ic), ft.IconButton(
       ft.icons.INFO, icon_size = 50, icon_color=ic)
     ])

#Input Section with Questions

a = ft.TextField(label="Enter Fasting Blood Glucose (mmol/l)",
          helper_text=""" Round to one decimal place. 
          Example: 5.5
          """, 
         max_length=4,keyboard_type = ft.KeyboardType.NUMBER,
         icon=ft.icons.PERSON, height = 110, text_size= 15)

fg = ft.Row(controls=[a]#alignment=ft.MainAxisAlignment.CENTER)
)

b = ft.TextField(label="Enter 2-hour Post-Prandial Blood Glucose (mmol/l)",
          helper_text=""" Round to one decimal place. 
          Example: 5.5
          """, 
         max_length=4,keyboard_type = ft.KeyboardType.NUMBER,
         icon=ft.icons.PERSON, height = 110, text_size= 15)#,
         #helper_style= ft.colors.WHITE)

thr = ft.Row(controls=[b]
) 

c= ft.TextField(label="Enter entry HbA1C (%):",
          helper_text=""" Round to one decimal place. 
          Example: 5.5
          """, max_length=4,keyboard_type = ft.KeyboardType.NUMBER,
          icon=ft.icons.PERSON, height = 110, text_size= 15)

mets = ft.Text("Does client have Metabolic Syndrome?", size= 15,color="black",
               weight=ft.FontWeight.BOLD)         

dmq = ft.Text("Previous Diagnosis with Type II DM:", size= 15,color="black",
               weight=ft.FontWeight.BOLD)         
hb = ft.Row(controls=[c])

snacka = ft.Row([])
snackb = ft.Row([])
space1=ft.Row([], vertical_alignment=ft.CrossAxisAlignment.END)
space2=ft.Row([], vertical_alignment=ft.CrossAxisAlignment.END)
space3=ft.Row([], vertical_alignment=ft.CrossAxisAlignment.END)
snackc = ft.Row([])
snackd = ft.Row([])
snack = ft.Column()
ansh = ft. Column([ft.Text("RECOMMENDATION", weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)], 
                          horizontal_alignment=ft.CrossAxisAlignment.CENTER)
ans = ft.Column()
ans_output= ft.Column([ansh,ans])


warning = ft.Text("""
                  NB: Dosages could change with presence of significant comorbidities such as 
                      renal impairment""" ,
                  italic=True,size=18, weight=ft.FontWeight.BOLD)
metformin = ft.Text("""
                Here are suggested dosing regimens:
                    
                METFORMIN
                Immediate release: Initial: Oral: 500 mg once or twice daily or 850 mg once daily.
                Usual maintenance dosage: Oral: 1 g twice daily or 850 mg twice daily (Ref).
                Maximum: Oral: 2.55 g/day.GI adverse effects may limit use.
                If doses >2 g/day are needed, consider administering in 3 divided doses to minimize GI adverse effects.
""")
dapa = ft.Text("""
               DAPAGLIFLOZIN
               Oral: Initial: 5 mg once daily; may increase to 10 mg once daily after 4 to 12 weeks. 
               In concomitant Heart Failure: 10mg once daily.""")
predmans2 = ft.Column([ft.Text(""" 
                        In addition to Metformin and Acarbose, Consider: 
                            
                        Thiazolidinediones such as Pioglitazone (with caution), or
                        Glucagon-Like Peptide-1 Receptor Agonists such as Exenatide, 
                        Liraglutide and Lixisenatide""", italic=True), 
                        ft.Text(""" 
                        PIOGLITAZONE:
                        Oral: Initial: 15mg daily. If inadequate glycemic control, escalate dose 4- to 12- weekly by 15mg to 
                        maximum of 45mg daily
                        
                        EXENATIDE:
                        Initial dose: 5 mcg subcutaneously, twice daily 
                        (within 1 hour before the 2 main meals of the day, at least 6 hours apart).
                        If inadequate glycemic control after 4 weeks,
                        increase dose as tolerated to 10 mcg subcutaneously twice daily.

                        LIRAGLUTIDE: 
                        Initial dose: 0.6 mg subcutaneously, once daily for 1 week and then increase to 
                        1.2 mg subcutaneously, once daily.
                        If inadequate glycemic control after another 1 to 2 weeks, increase dose as tolerated to 
                        1.8 mg subcutaneously once daily.
                            """, weight=ft.FontWeight.BOLD), warning])

        
 

predmans1 = ft.Column([ft.Text("Consider Metformin and Acarbose. Here are suggested dosing regimens:", size=20),ft.Text(
                         """
                         ACARBOSE: 
                        Oral: Initial: 25 mg once daily, then gradually titrate to 3 times daily, with the first bite of each main meal.
                        Increase dose at 4- to 8-week intervals based on 1-hour postprandial glucose or HbA1c levels and tolerance 
                        until maintenance dose of 50 to 100 mg 3 times daily is reached.
                        (maximum dose: ≤60 kg: 50 mg 3 times daily; >60 kg: 100 mg 3 times daily).
     
                         METFORMIN:
                        Immediate release: Oral: Initial: 850 mg once daily for 1 month, then increase to 850 mg twice daily; 
                        unless GI adverse effects warrant a longer titration period
                         """, weight=ft.FontWeight.BOLD), warning, ft.Text("""
                         If inadequate glycemic control persists, 
                         consider adding Thiazolidinediones such as Pioglitazone (with caution), or
                         Glucagon-Like Peptide-1 Receptor Agonist such as Exenatide, Liraglutide and Lixisenatide""")])
#Building Page

def main(page: ft.Page):
    page.bgcolor = "#EDEADE" 
    page.scroll = ft.ScrollMode.ALWAYS
    #page.auto_scroll = True
    page.window_min_height = 1250
    page.snack_bar = ft.SnackBar(content=snack)

    #page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    
    def dmalgo():
        
        try:
            num3 = float(c.value)
        except:
            num3 = 0
        
        if num3 == 0:
           pass
        elif num3 >= 9:
            ans.controls.append(ft.Column([ft.Text("""Consider DUAL THERAPY OR TRIPLE THERAPY with Metformin + one of: 
            Glucagon-Like Peptide-1 Receptor Agonists(GLP1-RA) such as Exenatide,Liraglutide, 
            or Sodium-glucose co-transporter-2 inhibitors (SGLT2i) such as Dapagliflozin and Canagliflozin,
            or Gliptins such as Vildagliptin,Linagliptin,Sitagliptin,
            or Thiazolidinediones such as Pioglitazone (with caution). 
            ADD OR INTENSIFY INSULIN based on insulin algorithm
            If there is concomitant Atherosclerotic cardiovascular disease: long-acting GLP1-RA or SGLT2i.
            If there is concomitant CKD Stage 3, consider a long-acting GLP1-RA or Canagliflozin.
            If there is concomitant HFrEF, consider a long-acting GLP1-RA or Dapagliflozin.
            """),metformin,dapa,warning,ft.Text("If there is inadequate glycemic control after 3 months, proceed to next level of therapy",
                                        italic=True,)]))
        elif num3 >=7.5 and num3 <=9:
            ans.controls.append(ft.Column([ft.Text("""Consider DUAL THERAPY OR TRIPLE THERAPY with Metformin + one of: 
            Glucagon-Like Peptide-1 Receptor Agonists(GLP1-RA)such as Exenatide,Liraglutide,
            or Sodium-glucose co-transporter-2 inhibitors (SGLT2i) 
            such as Dapagliflozin and Canagliflozin,
            or Gliptins such as Vildagliptin,Linagliptin,Sitagliptin,
            or Thiazolidinediones such as Pioglitazone (with caution). 
            If there is concomitant Atherosclerotic cardiovascular disease: long-acting GLP1-RA or SGLT2i.
            If there is concomitant CKD Stage 3, consider a long-acting GLP1-RA or Canagliflozin.
            If there is concomitant HFrEF, consider a long-acting GLP1-RA or Dapagliflozin.
            """), metformin,dapa,warning,ft.Text("If there is inadequate glycemic control after 3 months, proceed to next level of therapy",
                                        italic=True)]))
        else:
            ans.controls.append(ft.Column([ft.Text("""Consider MONOTHERAPY with one of: Metformin,Glucagon-Like Peptide-1 
            Receptor Agonists(GLP1-RA) such as Exenatide,Liraglutide, 
            or Sodium-glucose co-transporter-2 inhibitors such as Dapagliflozin and Canagliflozin,
            or Gliptins such as Vildagliptin,Linagliptin,Sitagliptin. 
            If there is concomitant Atherosclerotic cardiovascular disease: long-acting GLP1-RA or SGLT2i.
            If there is concomitant CKD Stage 3, consider a long-acting GLP1-RA or Canagliflozin.
            If there is concomitant HFrEF, consider a long-acting GLP1-RA or Dapagliflozin.
            """),metformin,dapa, warning],ft.Text("If there is inadequate glycemic control after 3 months, proceed to next level of therapy",
                                            italic=True)))
    def button_clicked(e):
        countdm = 0
        countpdm =0 
        try:
            num1 = float(a.value)
        except:
            num1 = 0
            
        try:
            num2 = float(b.value)
        except:
            num2 = 0
            
        try:
            num3 = float(c.value)
        except:
            num3 = 0
        
        if num1 == 0:
            pass
        elif num1 >= 7:
            snack.controls.append(ft.Text("Fasting Blood Glucose meets criteria for Type II Diabetes Mellitus", size = 25))
            countdm +=1
        elif num1 >=5.6 and num1 <=6.9:
            snack.controls.append(ft.Text("Fasting Blood Glucose meets criteria for Pre-Diabetes Mellitus (Type II)",size = 25))
            countpdm +=1
        else:
            snack.controls.append(ft.Text("Normal Fasting Blood Glucose results",size = 25))
            
        if num2 == 0:
            pass
        elif num2 >= 11.1:
            snack.controls.append(ft.Text("2-hour Post-Prandial Glucose meets criteria for Type II Diabetes Mellitus",size = 25))
            countdm +=1
        elif num2 >=7.8 and num2 <=11:
            snack.controls.append(ft.Text("2-hour Post Prandial Glucose meets criteria for Pre-Diabetes Mellitus (Type II)",size = 25))
            countpdm +=1
        else:
            snack.controls.append(ft.Text("Normal 2-hour Post Prandial Glucose results",size =25))
            
        if num3 == 0:
           pass
        elif num3 >= 6.5:
            snack.controls.append(ft.Text("HbA1C meets criteria for Type II Diabetes Mellitus",size =25))
            countdm +=1
        elif num3 >=5.7 and num3 <=6.4:
            snack.controls.append(ft.Text("HbA1C meets criteria for Pre-Diabetes Mellitus (Type II)",size =25))
            countpdm +=1
        else:
            snack.controls.append(ft.Text("Normal HbA1C results",size = 25))
            
        metans = m.value       
        if metans == True:
             snack.controls.append(ft.Text("Presence of Metabolic Syndrome meets criteria for Pre-Diabetes Mellitus (Type II)",size =25))
             countpdm +=1
        else:
             pass
         
        if dm.value != True: 
            if countdm == 0: 
                if countpdm >= 2:
                    ans.controls.append(predmans2)
            
                elif countpdm == 1:
                    ans.controls.append(predmans1)
            
            else:
                ans.controls.append(ft.Text("Treat according to the DM algorithm"))
                dmalgo()
        else: 
           dmalgo() 
        page.snack_bar.open = True
        page.update()
        
        
        
        
    enter = ft.FilledButton(text="Submit", on_click= button_clicked,icon="check",
                            style=ft.ButtonStyle(bgcolor=ft.colors.BLACK))
#Buttton Controls
   
    def cleared(e):
            
        a.value = ""
        b.value = ""
        c.value = ""
        m.value = False
        m.label = "No"
        dm.value = False
        dm.label = "No"
        snack.controls.clear()
        ans.controls.clear()

        page.update()
    
    clearall = ft.FilledTonalButton(text="Clear", on_click= cleared,icon= "close",
                               style=ft.ButtonStyle(bgcolor=ft.colors.BLUE_GREY_900))
    
    resets = ft.Row([enter,clearall])

            
    def metbutton(e):
        
        m.label = "Yes"
        m.value = True
                   
        page.update()

    m = ft.Switch(label="No", value=False, on_change=metbutton)
    
    def clearmet(e):
        
        m.label = "No"
        m.value = False
                   
        page.update()
        
    
    metc = ft.TextButton(text="Clear", on_click = clearmet, icon= "remove",
                   style=ft.ButtonStyle(color=ft.colors.BLUE_GREY_900), 
                icon_color = bc)                        
    
    
    metb=ft.Row([ft.Icon(name=ft.icons.PERSON, color="#808080"),mets,m,metc])
    def dmbutton(e):
        
        dm.label = "Yes"
        dm.value = True
                   
        page.update()

    dm = ft.Switch(label="No", value=False, on_change=dmbutton)
    
    def cleardm(e):
        
        dm.label = "No"
        dm.value = False
                   
        page.update()
        
    dmc = ft.TextButton(text="Clear", on_click = cleardm, icon= "remove",
                   style=ft.ButtonStyle(color=ft.colors.BLUE_GREY_900), 
                icon_color = bc)    
    dmrow=ft.Row([ft.Icon(name=ft.icons.PERSON, color="#808080"),dmq,dm,dmc])

    
    outline= ft.Row([ft.Column([ft.Column([ft.Text("Enter the following details:", size=20,text_align=ft.TextAlign.CENTER)],
               horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            ft.Text("""
                    NB: Results can be generated even if some sections have no input
                    If client has been previously diagnosed with Type II DM, 
                    the recommendations would be based on the HbA1C.
                    """, style=ft.TextThemeStyle.LABEL_MEDIUM),
        space1, fg,space2, thr,space3,hb,metb,dmrow,resets]),
                    ft.VerticalDivider(color=bc,width=9, thickness=3),ft.Container(content=ans_output,
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor= "#f8f8ff", #"#fcfcfc",
                        width=800,
                        height=800,
                        border_radius=10)])
                                
    layout=ft.Container(content=outline,
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor= "#FAF9F6",#bebfc0", #"#b6ccce#",
                    width=510,
                    height=750,
                    border_radius=10)
    
    
    #The following creates tabs for desktop view but not web view.
    # t = ft.Tabs(
    #     selected_index=0,
    #     animation_duration=100,
    #     tabs=[
    #         ft.Tab(
    #             icon=ft.icons.SEARCH,
    #             text="Start Here",
    #             content= ft.Column([
    #             ft.Container(content=outline,
    #                 margin=10,
    #                 padding=10,
    #                 alignment=ft.alignment.center,
    #                 bgcolor= "#FAF9F6",#bebfc0", #"#b6ccce#",
    #                 width=510,
    #                 height=700,
    #                 border_radius=10)
                
    #                             ]))
    #             ,
                    
    #         ft.Tab(
    #             text="Confirmed Type II DM",
    #             icon=ft.icons.PEOPLE,
    #             content=ft.Text("This is Tab 3")
    #         )
    #         ]
    #     )
        
                
    page.add(appbar,layout)

ft.app(target=main, port=8080,view=ft.WEB_BROWSER)

    