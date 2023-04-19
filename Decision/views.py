from django.shortcuts import render
from django.shortcuts import render
from django.core.files.images import ImageFile
from .forms import ImageForm
from .decision import predict
from tensorflow.keras.preprocessing import image

def predict_disease(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Call the predict function with the uploaded image
            img = ImageFile.open(request.FILES['image'])
            disease = predict(img)
            recommendation = "None"

            if disease == "rust":
                recommendation="Chemical control includes the use of fungicides such as Propiconazole, Triadimefon, Tebuconazole, and Azoxystrobin.Organic control includes crop rotation, using resistant varieties, proper pruning and proper irrigation."
            if disease == "Northern Leaf Blight":
                recommendation="Chemical control measures for this disease include the use of fungicides, such as chlorothalonil, mancozeb, and propiconazole. Organic control include crop rotation, planting disease-resistant varieties, and using cover crops to improve soil health and reduce the number of fragments of the fungus in the soil."
            if disease == "zincdeficiency":
                recommendation="Chemical control of zinc deficiency in maize involves the application of zinc fertilizers, such as zinc sulfate, to the soil. Organic control involves the use of organic amendments, such as compost, manures, and green manures, practicing crop rotation and planting cover plants that are known to accumulate zinc in the soil such as alfalfa or hairy vetch."
            if disease == "herbicideburn":
                recommendation = "Chemical control involves the application of a herbicide that is specifically formulated to control the weeds that are present in the field. Organic control of herbicide burn in maize involves using cultural and mechanical methods to control weeds, such as crop rotation, tillage, and hand weeding."
            if disease == "Fallarmyworm":
                recommendation= "Chemical control involves use of pesticides such as Bacillus thuringiensis (Bt) insecticides, pyrethroids, and neonicotinoids. Organic control involves planting varieties that are resistant to fall armyworms, crop rotation and encouraging natural predators that feed on the worms."
            if disease == "Cercospora":
                recommendation="Chemical control includes use of fungicides such as triazoles, strobilurins, and chlorothalonil. Organic control involves crop rotation, proper irrigation and soil fertility management."
            return render(request, 'result.html', {'disease': disease, 'recommendation': recommendation})
    else:
        form = ImageForm()
    return render(request, 'home.html', {'form': form})
