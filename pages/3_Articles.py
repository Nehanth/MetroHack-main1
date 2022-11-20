from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="Find your Disease",
    page_icon="🤔",
    layout="wide"
)


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_health = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_x1gjdldd.json")
lottie_welcome = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_puciaact.json")
lottie_disease = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_gkgqj2yq.json")
lottie_diabetes = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_tbjuenb2.json")
lottie_heart = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_zw7jo1.json")
lottie_heart2 = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_ftm7vjjr.json")
lottie_asthma = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_h1ufQIhlPX.json")
img_ms = Image.open("/Users/nehanthnarendrula/Downloads/MetroHack-main/images/multiple-sclerosis.jpg")
img_ms1 = Image.open("/Users/nehanthnarendrula/Downloads/MetroHack-main/images/Multiple_sclerosis.jpg")
img_heart = Image.open("/Users/nehanthnarendrula/Downloads/MetroHack-main/images/heart.jpg")
img_asthma = Image.open("/Users/nehanthnarendrula/Downloads/MetroHack-main/images/asthma.jpg")

# st.title("Main Page")
st.subheader("Learn More")
st_lottie(lottie_disease, height=300, key="disease")
st.title("Read articles about some common disease that are usually found in people.")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Diabetes")
        st.write("##")
        st.write(
            """
            Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy.
            Your body breaks down most of the food you eat into sugar (glucose) and releases it into your bloodstream. When your blood sugar goes up, it signals your pancreas to release insulin. Insulin acts like a key to let the blood sugar into your body’s cells for use as energy.
            With diabetes, your body doesn’t make enough insulin or can’t use it as well as it should. When there isn’t enough insulin or cells stop responding to insulin, too much blood sugar stays in your bloodstream. Over time, that can cause serious health problems, such as heart disease, vision loss, and kidney disease.
            There isn’t a cure yet for diabetes, but losing weight, eating healthy food, and being active can really help. Other things you can do to help:
            - Take medicine as prescribed.
            - Get diabetes self-management education and support.
            - Make and keep health care appointments.
            """
        )
        st.write("[Learn More](https://www.who.int/news-room/fact-sheets/detail/diabetes)")
    with right_column:
        st_lottie(lottie_diabetes, height=300, key="diabetes")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st_lottie(lottie_heart, height=300, key="heart")
        st.image(img_heart)

    with right_column:
        st.header("Heart Disease")
        st.write("##")
        st.write(
            """
            The term “heart disease” refers to several types of heart conditions. The most common type of heart disease in the United States is coronary artery disease (CAD), which affects the blood flow to the heart. Decreased blood flow can cause a heart attack.
            Sometimes heart disease may be “silent” and not diagnosed until a person experiences signs or symptoms of a heart attack, heart failure, or an arrhythmia. When these events happen, symptoms may include:
            - Heart attack: Chest pain or discomfort, upper back or neck pain, indigestion, heartburn, nausea or vomiting, extreme fatigue, upper body discomfort, dizziness, and shortness of breath.
            - Arrhythmia: Fluttering feelings in the chest (palpitations).
            - Heart failure: Shortness of breath, fatigue, or swelling of the feet, ankles, legs, abdomen, or neck veins.
            High blood pressure, high blood cholesterol, and smoking are key risk factors for heart disease. About half of people in the United States (47%) have at least one of these three risk factors.2 Several other medical conditions and lifestyle choices can also put people at a higher risk for heart disease, including:
            - Diabetes
            - Overweight and obesity
            - Unhealthy diet
            - Physical inactivity
            - Excessive alcohol use
           """
        )
        st.write("[Learn More](https://www.cdc.gov/heartdisease/about.htm)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Multiple Sclerosis")
        st.write("##")
        st.write(
            """
            Multiple sclerosis (MS) is a potentially disabling disease of the brain and spinal cord (central nervous system).
            In MS, the immune system attacks the protective sheath (myelin) that covers nerve fibers and causes communication problems between your brain and the rest of your body. Eventually, the disease can cause permanent damage or deterioration of the nerves.
            Signs and symptoms of MS vary widely and depend on the amount of nerve damage and which nerves are affected. Some people with severe MS may lose the ability to walk independently or at all, while others may experience long periods of remission without any new symptoms.
            There's no cure for multiple sclerosis. However, treatments can help speed recovery from attacks, modify the course of the disease and manage symptoms.
            Multiple sclerosis signs and symptoms may differ greatly from person to person and over the course of the disease depending on the location of affected nerve fibers. Symptoms often affect movement, such as:
            - Numbness or weakness in one or more limbs that typically occurs on one side of your body at a time, or your legs and trunk
            - Electric-shock sensations that occur with certain neck movements, especially bending the neck forward (Lhermitte sign)
            - Tremor, lack of coordination or unsteady gait
            Multiple sclerosis symptoms may also include:
            - Slurred speech
            - Fatigue
            - Dizziness
            - Tingling or pain in parts of your body
            - Problems with sexual, bowel and bladder function
            """
        )
        st.write(
            "[Learn More](https://www.mayoclinic.org/diseases-conditions/multiple-sclerosis/symptoms-causes/syc-20350269)")
    with right_column:
        st.image(img_ms)
        st.image(img_ms1)

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st_lottie(lottie_asthma, height=300, key="asthma")
        st.image(img_asthma)
    with right_column:
        st.header("Asthma")
        st.write("##")
        st.write(
            """
            Asthma is a condition in which your airways narrow and swell and may produce extra mucus. This can make breathing difficult and trigger coughing, a whistling sound (wheezing) when you breathe out and shortness of breath.
            For some people, asthma is a minor nuisance. For others, it can be a major problem that interferes with daily activities and may lead to a life-threatening asthma attack.
            Asthma can't be cured, but its symptoms can be controlled. Because asthma often changes over time, it's important that you work with your doctor to track your signs and symptoms and adjust your treatment as needed.
            Asthma signs and symptoms include:
            - Shortness of breath
            - Chest tightness or pain
            - Wheezing when exhaling, which is a common sign of asthma in children
            - Trouble sleeping caused by shortness of breath, coughing or wheezing
            - Coughing or wheezing attacks that are worsened by a respiratory virus, such as a cold or the flu
            For some people, asthma signs and symptoms flare up in certain situations:
            - Exercise-induced asthma, which may be worse when the air is cold and dry
            - Occupational asthma, triggered by workplace irritants such as chemical fumes, gases or dust
            - Allergy-induced asthma, triggered by airborne substances, such as pollen, mold spores, cockroach waste, or particles of skin and dried saliva shed by pets (pet dander)
           """
        )
        st.write(
            "[Learn More](https://www.mayoclinic.org/diseases-conditions/asthma/symptoms-causes/syc-20369653#:~:text=Asthma%20is%20a%20condition%20in,asthma%20is%20a%20minor%20nuisance.)")