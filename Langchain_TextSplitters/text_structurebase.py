from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """The Skyward Shift: How Drones Are Reshaping Modern Agriculture
Agriculture has entered a new era driven by data, automation, and precision. Facing the dual pressures of climate volatility and a rapidly expanding global population, the farming sector must produce higher yields with fewer natural resources. At the forefront of this technological shift are Unmanned Aerial Vehicles (UAVs)—commonly known as drones. By bridging the gap between high-altitude satellite imagery and labor-intensive ground scouting, agricultural drones have evolved into vital instruments of modern precision farming.
The primary value of agricultural drones lies in their ability to monitor crop health with extraordinary precision. Traditional field inspections rely on manual sampling, which is slow and often misses subtle stressors until significant damage has already occurred. In contrast, drones equipped with multispectral, hyperspectral, and thermal sensors can survey hundreds of acres in a single flight. These sensors capture spectral signatures invisible to the human eye, calculating vegetative indices such as the Normalized Difference Vegetation Index (NDVI). By analyzing chlorophyll levels and light reflection, drones pinpoint early signs of nutrient deficiency, fungal infections, and pest attacks days or even weeks before visible symptoms emerge, allowing farmers to intervene before widespread damage sets in.
Beyond passive surveillance, drones actively execute precision field operations. In chemical application, specialized agricultural spraying drones use GPS positioning and flow-rate controllers to deliver micro-doses of pesticides, herbicides, and liquid fertilizers directly to affected areas. This targeted application cuts overall chemical usage by up to 30% to 40%, drastically lowering input costs, curbing toxic runoff into local waterways, and protecting human operators from direct chemical exposure. Furthermore, drones are increasingly used for direct seeding in hard-to-reach terrains, topographic 3D mapping for drainage management, and thermal tracking of livestock across vast pastures.
Despite these significant advantages, widespread adoption still faces several operational hurdles. The initial capital investment for enterprise-grade drones, specialized payloads, and advanced data-processing software can be prohibitive for smallholder farmers. Operational limitations—such as short battery life (often capped at 20 to 40 minutes per charge), sensitivity to adverse weather conditions, and strict national aviation regulations regarding Beyond Visual Line of Sight (BVLOS) operations—also present persistent challenges. Moreover, converting gigabytes of raw aerial imagery into actionable farming decisions requires technical literacy and robust data pipelines that many traditional operations lack.
Looking forward, the convergence of drone hardware with artificial intelligence and Edge computing promises to resolve many of these bottlenecks. Autonomous docking and charging stations are enabling scheduled, uncrewed missions, while onboard machine learning models can classify weeds and pests in real time during flight. When integrated alongside IoT soil sensors, automated irrigation systems, and autonomous tractors, drones form the central aerial intelligence layer of the modern farm ecosystem.
In conclusion, drones represent far more than a passing novelty in farming. By transforming reactive practices into proactive, data-driven decisions, drone technology empowers the agricultural sector to maximize crop productivity, conserve critical resources, and build a more resilient global food supply.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0
)

chunks = splitter.split_text(text)

print(f"Number of chunks: {len(chunks)}")
print(chunks)
