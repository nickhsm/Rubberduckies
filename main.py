import streamlit
import keras_model

streamlit.title("PCview")
streamlit.text("Met deze programma kan je computer onderdelen herkennen door een foto te uploaden. Er wordt vervolgens uitgelegd wat de onderdelen voor dienen.")

with streamlit.form("Foto upload form"):
    streamlit.text("Upload de foto en klik op upload")
    image = streamlit.file_uploader("Upload hier je foto", type=["jpg", "jpeg", "png"])
    streamlit.form_submit_button("Upload")

if image is not None:
    result = keras_model.ai_model(image)
    confidence_score = result["Confidence Score"]
    component = result["Class"]

    # Debug
    streamlit.write(result)

    streamlit.title("Resultaat")
    streamlit.write(f'We zijn met {confidence_score * 100}% zeker dat dit een {component} is.')
    
    streamlit.title("Uitleg")
    match component:
        case "PSU":
            streamlit.markdown(" \
                    Een power supply unit, afgekort PSU, of voeding in het Nederlands dient om de computer van stroom te voorzien. \
                    Dit wordt gedaan doormiddel van veschillende connectoren te gebruiken voor verschillende onderdelen. \
                    Zonder dit kan de computer niet opstarten. \
                    ")
        case "CPU":
            streamlit.markdown(" \
                    Een central processing unit, afgekort CPU, of processor in het Nederlands dient als een centrale rekenmachine. \
                    Kort door de bocht, een processor is een klein plaatje gemaakt van zand. Met behulp van UV-straling kunnen we kanalen maken met sluizen. \
                    Deze sluizen kunnen open en dicht, respectievelijk in computer term een 1 en een 0. \
                    Zonder dit kan de computer niet opstarten. \
                    ")
        case _:
            streamlit.markdown(" \
                    Hier is iets fout gelopen. \
                    ")
