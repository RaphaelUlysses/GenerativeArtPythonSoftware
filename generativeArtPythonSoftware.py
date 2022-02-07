import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageFont, ImageDraw 
import random

def orcSequence(uiResults):
        
    ## Variable Declaration
    imageWidth = 2160
    imageHeight = 2160
    verticalMargin = 40

    #Selected Background & Skintone
    shadowToneArray = ["rgb(0,0,0)","rgb(68,114,102)","rgb(56,101,52)","rgb(155,60,31)","rgb(115,69,186)"]
    lightToneArray =  ["rgb(25,25,25)","rgb(125,160,152)","rgb(128,185,123)","rgb(224,108,72)", "rgb(182,149,244)"]
    backgroundColorArray = ["rgb(199, 234, 229)", "rgb(255,64,123)", "rgb(67,202,255)", "rgb(175,226,159)", "rgb(25,25,25)", "rgb(255,170,0)", "rgb(0,0,0)"]


    #Permanent Ghost Colors
    ghostShadow = "rgb(18,100,153)"
    ghostLight = "rgb(95,165,210)"
    ghostOutline = "rgb(1,49,80)"
    ghostColor = "rgb(150,205,234)"



    #Array Determination
    #skinTone = ["Green","Teal","Burnt","Charcoal"]
    orcSegment = ["Base","Hand","BaseArmed","LeftEar","HeadBase","Head","LeftEye","Nose","RightEye","Jaw","RightEar"]
    segmentLayer = ["Skin", "ShadowSkin", "Color", "Blood", "Outline"]
    assetDirectory = "G:\\My Drive\\Projects\\BloodstainedOrks\\Assets\\"




    def assembleSegment (orcSegmentInput, orcSelectionInput, version, colorChangeArray, selectedShadow, selectedLight, headMask = "empty"):
        # from PIL import Image
        #PART_NUMBER_LAYER
        if orcSegmentInput == "000":
            return
        #Loads the background image created in main()
        #assetLoad = buildingSegment
        buildingSegment = Image.new(mode = "RGBA", size = (imageWidth, imageHeight), color = (0,0,0,0))
        assetLoad = Image.new(mode = "RGBA", size = (imageWidth, imageHeight), color = (0,0,0,0))
        #iterates through the segment layers in order of proper assembly (Base, LeftEar, HeadBase, LeftEye, Nose, RightEye, Jaw, RightEar)
        for layer in segmentLayer:
            if version != 2 and layer == "Blood":
                continue
            assetPath = assetDirectory + orcSegmentInput + "\\" + orcSegmentInput + "_" + orcSelectionInput + "_" + layer + ".png"
            assetPath = assetDirectory + orcSegmentInput + "\\" + orcSegmentInput + "_" + orcSelectionInput + "_" + layer + ".png"
            #try catch for expected file not found errors
            try:
                #loads the asset assembled from the Path string above
                assetLoad = Image.open(assetPath, "r").convert('RGBA')
                #if provided colorChangeArray contains certain strings script will infer the ORC version (normal, ghost, blood) and adjust color for correction.
                #If layer does not exist in array it will apply without color correction
                if layer in colorChangeArray:
                    #if else chain determines which entry was discovered in array
                    if "Outline" in layer:
                        appliedColor = ghostOutline
                    elif "Color" in layer:
                        appliedColor = ghostColor
                    elif "Shadow" in layer: 
                        appliedColor = selectedShadow
                    else:
                        appliedColor = selectedLight
                    alphaChannel = assetLoad.getchannel('A')
                    colorChangeObject = Image.new(mode = "RGBA", size = assetLoad.size, color=appliedColor)
                    colorChangeObject.putalpha(alphaChannel)
                    assetLoad = colorChangeObject
            except Exception:
                pass
            buildingSegment = Image.alpha_composite(buildingSegment, assetLoad)
        completeSegment = buildingSegment
        return completeSegment

    def assembleOrc (selectionMatrix, orcResult, version, colorChangeArray, selectedShadow, selectedLight):
        #todo: Add mismatched array size catch
        for selection, segment in zip(selectionMatrix, orcSegment):
            if selectionMatrix[1] == "000" and segment == "BaseArmed":
                continue
            orcResult = Image.alpha_composite(orcResult, assembleSegment(segment, selection, version, colorChangeArray, selectedShadow, selectedLight))
        return orcResult



    def main():
        #main requests go here
        x = "001"
        for R in range(1, uiResults.selectedQuantity):
            backgroundColor = backgroundColorArray[random.randint(0,6)]
            skinToneSelect = random.randint(0,4)
            #skinToneSelect = 1
            shadowTone = shadowToneArray[skinToneSelect]
            lightTone = lightToneArray[skinToneSelect]

            if uiResults.mode == "Random":
                leftEarRand = f'{random.randint(1,1):03d}'
                baseRand = f'{random.randint(1,32):03d}'
                handRand = f'{random.randint(1,21):03d}'
                headBaseRand = f'{random.randint(1,1):03d}'
                headRand = f'{random.randint(1,24):03d}'
                eyesRand = f'{random.randint(1,33):03d}'
                noseRand = f'{random.randint(1,11):03d}'
                jawRand = f'{random.randint(1,26):03d}'
                rightEarRand = f'{random.randint(1,1):03d}'
                selectionMatrix = [baseRand, handRand, baseRand, leftEarRand,headBaseRand, headRand, eyesRand, noseRand, eyesRand ,jawRand, rightEarRand]
            else:
                leftEarRand = "000"
                baseRand = "000"
                handRand = "000"
                headBaseRand = "000"
                headRand = "000"
                eyesRand = "000"
                noseRand = "000"
                jawRand = "000"
                rightEarRand = "000"
                selectionMatrix = [baseRand, handRand, baseRand, leftEarRand,headBaseRand, headRand, eyesRand, noseRand, eyesRand ,jawRand, rightEarRand]
        
            #if int(baseRand) > 11:
             #   handRand = "000"
            #else:
            handUpFlip = random.randint(0,1)
            if handUpFlip == 0:
                handRand = "000"
       
        
            R = f'{R:03d}'

            selectionMatrix = [baseRand, handRand, baseRand, leftEarRand,headBaseRand, headRand, eyesRand, noseRand, eyesRand ,jawRand, rightEarRand]

            orcResult = Image.new(mode = "RGBA", size = (imageWidth, imageHeight), color = backgroundColor)

            #Iterates through all 3 ORC Versions.
            # If y == 1 result will be Bloodstained Version
            # If y == 1 result will be Ghost Version
            for y in range(0,1):
                selectedShadow = shadowTone
                selectedLight = lightTone
                colorChangeArray = ["Skin","ShadowSkin"]
                print(y)
                if y == 1:
                    selectedShadow = ghostShadow
                    selectedLight = ghostLight
                    colorChangeArray = ["Skin","ShadowSkin","Color","Outline"]
                orcResult = assembleOrc(selectionMatrix, orcResult, y, colorChangeArray, selectedShadow, selectedLight)
                orcResult.save(assetDirectory+ "Output\\" + str(R) + "_" + str(y) + ".png" ,dpi=(600, 600))
                #orcResult.show()
        return ()

    main()  







class submissionResults:
    def __init__(self, mode, mainSegment, mainSegmentID, mainSequential, additionalSegment, additionalSegmentID, additionalSequential, selectedQuantity):
        self.mode = mode
        self.mainSegment = mainSegment
        self.mainSegmentID = mainSegmentID
        self.mainSequential = mainSequential
        self.additionalSegment = additionalSegment
        self.additionalSegmentID = additionalSegmentID
        self.additionalSequential = additionalSequential
        self.selectedQuantity = selectedQuantity


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('GAPS')
        self.geometry("700x700")
        
        
        self.quantity = tk.StringVar()
        self.sequentialOrder = tk.StringVar()
        self.additionalSequentialOrder = tk.StringVar()
        self.segmentID= tk.StringVar()
        self.segmentSelection = tk.StringVar()
        self.additionalSegmentSelection = tk.StringVar()
        self.additionalSegmentID = tk.StringVar()
        self.additionalSegmentIDSelection = tk.StringVar()
        self.modeSelectValue = tk.StringVar()
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        
        self.create_widgets()

    def create_widgets(self):
        
 
        #Due to trace function limitations the StringVar does not get passed into the callback function. As such we need a seperate callback for each item
        def modeCallback(*args):
            result = str(self.modeSelectValue.get())
            if result == "Test":
                quantity_entry.config(state='disabled')
            if result == "Production":
                quantity_entry.config(state='disabled')
            if result == "Random":
                segmentTestSelect.config(state='disabled')
                segmentIDSelection.config(state='disabled')
                sequentialSelection.config(state='disabled')
                additionalSequentialSelection.config(state='disabled')
                additionalSelect.config(state='disabled')
                additionalSegmentIDSelection.config(state='disabled')
            print (self)
            type(self)

        #Callback for the main segment selection
        def segmentCallback(*args):
            print (self)
            type(self)
        
        #Callback for main segment sequential button
        def sequentialCallback(*args):
            if self.sequentialOrder.get() == "1":
                   # ttk.Label(self, text='Quantity will equal segment upper limit').grid(column=2, row=1, **padding)
                    segmentIDSelection.config(state='disabled')
            else:
                segmentIDSelection.config(state='enabled')

        #Callback for additional segment sequential button
        def additionalSequentialCallback(*args):
            if self.additionalSequentialOrder.get() == "1":
                # ttk.Label(self, text='Quantity will equal segment upper limit').grid(column=2, row=1, **padding)
                additionalSegmentIDSelection.config(state='disabled')
            else:
                additionalSegmentIDSelection.config(state='enabled')
        
        
        def additionalSegmentCallback(*args): 
           result = str(self.modeSelectValue.get())
        
           
        padding = {'padx': 10, 'pady': 10}
        #Row 0
        row = 0
        ttk.Label(self, text='Mode').grid(column=0, row=row, **padding)
        modeOptions = ["Test","Production","Random"]
        modeSelection = ttk.OptionMenu(self , self.modeSelectValue , "(Select Mode)",  *modeOptions )
        modeSelection.grid(column=1, row=row, **padding)
        self.modeSelectValue.trace_variable('w', modeCallback)

        #Row 1
        row = 1
        ttk.Label(self, text='Quantity:').grid(column=0, row=row, **padding)
        quantity_entry = ttk.Entry(self, textvariable=self.quantity)
        quantity_entry.grid(column=1, row= row, **padding)

        #Row 2
        row = 2
        ttk.Label(self, text='Main Segment:').grid(column=0, row=row, **padding)
        orcSegment = ["Base","Hand","BaseArmed","LeftEar","HeadBase","Head","LeftEye","Nose","RightEye","Jaw","RightEar"]
        segmentTestSelect = ttk.OptionMenu(self , self.segmentSelection , "(Select Segment)",  *orcSegment )
        segmentTestSelect.grid(column=1, row=row, **padding)
        self.segmentSelection.trace_variable('w', segmentCallback)
        ttk.Label(self, text='Segment ID').grid(column=2, row=row, **padding)
        segmentIDSelection= ttk.Entry(self, textvariable=self.segmentID)
        segmentIDSelection.grid(column=3, row= row, **padding)
        sequentialSelection = ttk.Checkbutton(self, text = "Sequential Order", variable = self.sequentialOrder, onvalue = 1, offvalue=0)
        sequentialSelection.grid(column=4, row=row, **padding)
        self.sequentialOrder.trace_variable('w', sequentialCallback)


        #Row 3
        row = 3
        ttk.Label(self, text='Additional Segment:').grid(column=0, row=row, **padding)
        orcSegment = ["Base","Hand","BaseArmed","LeftEar","HeadBase","Head","LeftEye","Nose","RightEye","Jaw","RightEar"]
        additionalSelect = ttk.OptionMenu(self , self.additionalSegmentSelection , "(Select Segment)",  *orcSegment )
        additionalSelect.grid(column=1, row=row, **padding)
        self.additionalSegmentSelection.trace_variable('w', additionalSegmentCallback)
        ttk.Label(self, text='Segment ID').grid(column=2, row=row, **padding)
        additionalSegmentIDSelection= ttk.Entry(self, textvariable=self.additionalSegmentID)
        additionalSegmentIDSelection.grid(column=3, row= row, **padding)
        additionalSequentialSelection = ttk.Checkbutton(self, text = "Sequential Order", variable = self.additionalSequentialOrder, onvalue = 1, offvalue=0)
        additionalSequentialSelection.grid(column=4, row=row, **padding)
        self.additionalSequentialOrder.trace_variable('w', additionalSequentialCallback)
        
        
        # Button
        submit_button = ttk.Button(self, text='Submit', command=self.submit)
        submit_button.grid(column=2, row=0, **padding)

            
        

    
 

    def submit(self):
        mode = str(self.modeSelectValue.get())
        mainSegment = str(self.segmentSelection.get())
        try:
           mainSegmentID = int(self.segmentID.get())
        except:
           mainSegmentID = "000"
        if (self.sequentialOrder.get() == 1):
            mainSequential = True
        else: 
            mainSequential = False
        additionalSegment = str(self.additionalSegmentSelection.get())
        try:
            additionalSegmentID = int(self.additionalSegmentID.get())
        except:
           additionalSegmentID = "000"
        if (self.additionalSequentialOrder.get() == 1):
            additionalSequential = True
        else: 
            additionalSequential = False
        if int(self.quantity.get()) > 1:
            selectedQuantity = int(self.quantity.get())+1
        else:
            selectedQuantity = 1
        uiResults = submissionResults(mode, mainSegment, mainSegmentID, mainSequential, additionalSegment, additionalSegmentID, additionalSequential, selectedQuantity)


        orcSequence(uiResults)



if __name__ == "__main__":
    app = App()
    app.mainloop()
    






