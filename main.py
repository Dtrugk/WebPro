from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from vertexai.preview.language_models import ChatModel, InputOutputTextPair,ChatSession,CodeChatModel
from google.cloud import aiplatform

app = Flask(__name__)
app.secret_key = "your_secret_key"  

chat_model = ChatModel.from_pretrained("chat-bison@001")


chat_model2 = CodeChatModel.from_pretrained("codechat-bison@001")


@app.route("/",methods =["GET","POST"])
def landing():
    if request.method == "POST":
        username = request.form.get("username")
        # Store the username in the session
        session["username"] = username
        return redirect(url_for("home"))
    return render_template("index.html")

@app.route("/home")
def home():
    username = session.get("username")
    # username = chatbot.chat()
    return render_template("home.html",username=username)

@app.route("/Chatbot",methods =["GET","POST"])
def chat():
    chat = ChatSession(chat_model)
    # TODO developer - override these parameters as needed:
    parameters = {
        "temperature": 0.5,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 1024,  # Token limit determines the maximum amount of text output.
        "top_p": 0.95,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
        "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.
    }

    Example = InputOutputTextPair(
        input_text="What are you?",
        output_text="I'm a AI language model"
    )

    Example2 = InputOutputTextPair(
        input_text="How to crack an eggs",
        output_text="To crack an egg, gently tap the egg on a hard surface, such as the counter or a bowl. Then, using your fingers, gently spread the shell apart and open the egg.",
    )

    Example3 = InputOutputTextPair(
        input_text="What is the process of photosynthesis?",
        output_text="Photosynthesis is the process by which green plants, algae, and some bacteria convert light energy from the sun into chemical energy. During this process, carbon dioxide and water are combined, and with the help of sunlight and chlorophyll, they produce glucose and oxygen as byproducts."
    )

    Example4 = InputOutputTextPair(
        input_text="How does encryption work in computer systems?",
        output_text="Encryption is a technique used to secure data and communications in computer systems. It involves converting plaintext into ciphertext using an algorithm and a key. The encrypted data can only be decrypted back to its original form by someone with the corresponding decryption key. This ensures that sensitive information remains confidential and secure from unauthorized access."
    )

    Example5 = InputOutputTextPair(
        input_text="What are the basic concepts of object-oriented programming?",
        output_text="Object-oriented programming (OOP) is a programming paradigm that focuses on the concept of objects, which encapsulate data and behavior. The basic concepts in OOP include classes, objects, inheritance, polymorphism, and encapsulation. Classes serve as blueprints for creating objects, while inheritance allows classes to inherit properties and methods from other classes. Polymorphism enables objects to be treated as instances of their parent classes, and encapsulation hides the internal details of an object, exposing only necessary interfaces to the outside world."
    )

    Example6 = InputOutputTextPair(
        input_text="What are the key characteristics of the Spanish language?",
        output_text="AI: Spanish, or Español, is a Romance language with several key characteristics. It is widely spoken across many countries, making it one of the most spoken languages globally. Spanish uses the Latin alphabet and has a phonetic system where words are generally pronounced as they are written. It also contains various accents and dialects, depending on the region. Additionally, Spanish is known for its gendered nouns and complex verb conjugations, which give the language its unique structure and grammar rules."
    )

    Example7 = InputOutputTextPair(
        input_text="User: Who wrote the famous play 'Romeo and Juliet'?",
        output_text="AI: 'Romeo and Juliet'  is a famous tragedy written by William Shakespeare, an English playwright and poet. It was first published in 1597 and has since become one of the most iconic and enduring works in the literary world. The play tells the tragic tale of two young lovers from feuding families, the Capulets and the Montagues, and their ill-fated romance."
    )

    Example8 = InputOutputTextPair(
        input_text="What is the theory of relativity?",
        output_text="AI: The theory of relativity is a fundamental theory in physics proposed by Albert Einstein. It comprises two major parts: the special theory of relativity and the general theory of relativity. The special theory of relativity, published in 1905, deals with objects moving at constant velocities in inertial frames of reference and introduces concepts like time dilation and length contraction. The general theory of relativity, published in 1915, extends these principles to include gravity, describing it as the curvature of spacetime caused by the presence of mass and energy."
    )

    Example9 = InputOutputTextPair(
        input_text="How do algorithms work, and why are they important in computer science?",
        output_text="Algorithms are step-by-step procedures or sets of rules used to solve specific problems or perform specific tasks in computer science. They take input data and process it through a series of well-defined steps to produce an output or achieve a desired goal. Algorithms play a crucial role in computer science as they form the foundation for software development, data analysis, artificial intelligence, and much more. Efficient algorithms can significantly impact the performance and speed of computer programs and systems."
    )

    Example10 = InputOutputTextPair(
        input_text="how to build a car ?",
        output_text='''Building a car is an incredibly complex and specialized task that requires extensive engineering knowledge, advanced manufacturing facilities, and a team of skilled professionals. It involves design, prototyping, testing, safety compliance, and many other stages that are beyond the scope of a simple tutorial.

                        However, I can provide you with a high-level overview of the key steps involved in building a car:

                        Concept and Design: The process begins with defining the concept of the car and creating detailed design plans. Engineers and designers work together to determine the car's specifications, features, dimensions, and aesthetics.

                        Engineering and Prototyping: Once the design is finalized, engineers create computer models and prototypes to test the car's performance, safety, and efficiency. This stage involves extensive simulations and analysis.

                        Material Selection: Choose the appropriate materials for different components of the car, considering factors like strength, weight, cost, and manufacturability.

                        Manufacturing: Actual production starts with manufacturing different parts of the car, including the chassis, engine, transmission, body panels, interior components, and more. This involves various manufacturing processes like stamping, molding, welding, and assembly.

                        Quality Control and Testing: Every component undergoes rigorous quality control checks to ensure they meet the required standards. The car is also subjected to a series of tests for safety, performance, and reliability.

                        Assembly: After the individual parts are manufactured and tested, they are assembled together to form the complete car. This involves integrating the engine, transmission, suspension, electrical systems, and all other components.

                        Painting and Finishing: The car's body is painted and finished to give it the desired appearance and protection against corrosion.

                        Testing and Certification: The fully assembled car undergoes extensive testing, including road tests, crash tests, emission tests, and more. It must meet various safety and environmental regulations before being certified for sale.

                        Marketing and Distribution: Once the car is ready for the market, marketing and distribution strategies are put in place to make it available to consumratch as an individual is not practical or safe. If you are interested in automobiles and engineering, consider exploring careers in automotive design, engineering, or manufacturing.'''
    )

    Example11 = InputOutputTextPair(
        input_text="How gun powder was made ?",
        output_text="Gunpowder, also known as black powder, was traditionally made by grinding and mixing potassium nitrate (saltpeter), charcoal, and sulfur in specific proportions. The mixture was wetted with water, shaped into pellets, and dried. The resulting gunpowder was used in firearms and other military applications. Please note that gunpowder production can be hazardous and should only be attempted in controlled industrial settings following safety protocols."
    )

    Example12 = InputOutputTextPair(
        input_text="How to learn a new language ?",
        output_text='''Set clear goals for learning the language.
                        Choose reputable learning resources.
                        Practice regularly and immerse yourself in the language.
                        Focus on pronunciation and basic phrases.
                        Use flashcards and repetition for vocabulary.
                        Learn grammar fundamentals.
                        Practice speaking with native speakers.
                        Be patient, persistent, and stay motivated.'''
    )

    Example13 = InputOutputTextPair(
        input_text="Tell me a story",
        output_text='''In the enchanting land of Elaria, lived a young and curious girl named Lila. She loved exploring the vast forests around her village. One day, she found a hidden path and was transported to Elysium, a realm of wonder and magic.

                        In Elysium, Lila met Finn, a mischievous but kind-hearted fox. Together, they roamed the magical landscapes, helping creatures in need. They learned about the true essence of magic - love, empathy, and respect for all living beings.

                        Elysium was in danger from an evil sorceress, the Enchantress of Shadows. She sought the Amethyst Crystal to plunge the realm into darkness. Lila and Finn embarked on a quest to find the crystal and faced many challenges.

                        With the Amethyst Crystal's brilliance, Lila defeated the Enchantress and saved Elysium. The creatures celebrated them as heroes.

                        As the sun set, Lila returned to Elaria, carrying the magic of Elysium in her heart. Her adventurous spirit continued, knowing that kindness and courage could lead to extraordinary journeys. The tale of Lila's adventure became a cherished legend, inspiring generations with the power of love and magic.'''
    )

    Example14 = InputOutputTextPair(
        input_text="How data being transfer via internet ?",
        output_text='''Data is transferred over the internet through a network of interconnected devices. The process involves data encoding into binary code, dividing it into packets, adding destination addresses, and error-checking data. Routers determine the best path for each packet to reach its destination. The packets are transmitted through communication channels like fiber-optic cables or wireless connections.

                        The internet backbone, consisting of high-speed networks, connects major hubs and data centers, facilitating long-distance data transfer. Intermediary devices, such as switches and routers, direct packets along the optimal path.

                        At the destination, packets are reassembled to reconstruct the original data. During the transfer, acknowledgments are sent back to confirm successful receipt, and error-checking mechanisms request retransmission for any lost or corrupted packets.

                        TCP/IP is the foundational protocol suite for internet communication, ensuring reliable and orderly data delivery. This dynamic process enables users to access websites, send emails, and interact across the internet, making it essential for our interconnected world.'''
    )


    Example16 = InputOutputTextPair(
        input_text="Protocol in network layer ",
        output_text='''In the network layer of the OSI (Open Systems Interconnection) model and the Internet layer of the TCP/IP model, there are several key protocols that play essential roles in routing and forwarding data packets across networks. These protocols facilitate the delivery of data to their intended destinations. Some of the most notable protocols in the network layer are:

                        Internet Protocol (IP): The Internet Protocol (IP) is the fundamental protocol of the network layer. It provides the addressing scheme and routing mechanisms to deliver data packets across interconnected networks, ensuring data reaches its destination.

                        Internet Control Message Protocol (ICMP): ICMP is used for error reporting, diagnostics, and management of network devices. It is often used to check the availability and responsiveness of network hosts through tools like ping.

                        Internet Group Management Protocol (IGMP): IGMP is used to manage multicast group membership. It allows devices to join and leave multicast groups to receive specific data streams efficiently.

                        Routing Information Protocol (RIP): RIP is a distance-vector routing protocol that helps routers exchange routing information and determine the best paths for forwarding packets.

                        Open Shortest Path First (OSPF): OSPF is a link-state routing protocol that calculates the shortest path to each network by considering the link's cost. It is widely used in large-scale networks.

                        Border Gateway Protocol (BGP): BGP is a path-vector routing protocol used for exchanging routing information between autonomous systems (AS). It is the primary protocol that enables communication between different internet service providers (ISPs).

                        Enhanced Interior Gateway Routing Protocol (EIGRP): EIGRP is a Cisco proprietary routing protocol designed to efficiently exchange routing information and reduce convergence time in a network.

                        These protocols work together to ensure efficient and reliable data transmission in computer networks. IP, being the core protocol of the network layer, plays a central role in determining the route that data packets take from the source to the destination. Other protocols, like ICMP, assist in network troubleshooting and diagnostics. The combination of these protocols enables data to navigate through complex networks and reach its intended recipients.'''
    )

    Example17 = InputOutputTextPair(
        input_text="Transport layer protocols",
        output_text='''In the transport layer of the OSI (Open Systems Interconnection) model and the transport layer of the TCP/IP model, there are two primary protocols that are commonly used:

                        Transmission Control Protocol (TCP): TCP is a connection-oriented protocol that ensures reliable data delivery between applications. It establishes a connection between the sender and receiver before data transfer, and it guarantees that data packets are delivered in the correct order without loss or duplication. TCP also handles flow control, ensuring that data is sent at a rate suitable for the receiver's capacity to process it. It is widely used for applications that require error-free and ordered data transmission, such as web browsing, file transfers, and email.

                        User Datagram Protocol (UDP): UDP is a connectionless protocol that provides a lightweight, fast, and simple method for sending datagrams (packets) from one host to another. Unlike TCP, UDP does not establish a connection before data transfer and does not guarantee reliable delivery or packet ordering. As a result, UDP is considered less reliable than TCP but is preferred for real-time applications like audio and video streaming, online gaming, and VoIP (Voice over Internet Protocol). These applications can tolerate some data loss and are more concerned with minimizing latency.

                        Both TCP and UDP serve distinct purposes and are used based on the specific requirements of the applications they support. TCP is ideal for applications that prioritize data integrity and accuracy, while UDP is suitable for applications where low latency and speed are essential, and some data loss can be tolerated.'''
    )

    if request.method == "POST":
        usr = request.form.get("userinput")
        response = chat.send_message(usr, **parameters)
        return jsonify({"response": response})
    else:
        return render_template("Chatbot.html")
    

@app.route("/chatbot2",methods =["GET","POST"])
def chat2():
    chat2 = chat_model2.start_chat()
    # TODO developer - override these parameters as needed:
    parameters = {
        "temperature": 0.5,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 1024,  # Token limit determines the maximum amount of text output.
    }

    Example4 = InputOutputTextPair(
        input_text="How does encryption work in computer systems?",
        output_text="Encryption is a technique used to secure data and communications in computer systems. It involves converting plaintext into ciphertext using an algorithm and a key. The encrypted data can only be decrypted back to its original form by someone with the corresponding decryption key. This ensures that sensitive information remains confidential and secure from unauthorized access."
    )

    Example5 = InputOutputTextPair(
        input_text="What are the basic concepts of object-oriented programming?",
        output_text="Object-oriented programming (OOP) is a programming paradigm that focuses on the concept of objects, which encapsulate data and behavior. The basic concepts in OOP include classes, objects, inheritance, polymorphism, and encapsulation. Classes serve as blueprints for creating objects, while inheritance allows classes to inherit properties and methods from other classes. Polymorphism enables objects to be treated as instances of their parent classes, and encapsulation hides the internal details of an object, exposing only necessary interfaces to the outside world."
    )


    Example9 = InputOutputTextPair(
        input_text="How do algorithms work, and why are they important in computer science?",
        output_text="Algorithms are step-by-step procedures or sets of rules used to solve specific problems or perform specific tasks in computer science. They take input data and process it through a series of well-defined steps to produce an output or achieve a desired goal. Algorithms play a crucial role in computer science as they form the foundation for software development, data analysis, artificial intelligence, and much more. Efficient algorithms can significantly impact the performance and speed of computer programs and systems."
    )


    Example11 = InputOutputTextPair(
        input_text="How gun powder was made ?",
        output_text="Gunpowder, also known as black powder, was traditionally made by grinding and mixing potassium nitrate (saltpeter), charcoal, and sulfur in specific proportions. The mixture was wetted with water, shaped into pellets, and dried. The resulting gunpowder was used in firearms and other military applications. Please note that gunpowder production can be hazardous and should only be attempted in controlled industrial settings following safety protocols."
    )


    Example14 = InputOutputTextPair(
        input_text="How data being transfer via internet ?",
        output_text='''Data is transferred over the internet through a network of interconnected devices. The process involves data encoding into binary code, dividing it into packets, adding destination addresses, and error-checking data. Routers determine the best path for each packet to reach its destination. The packets are transmitted through communication channels like fiber-optic cables or wireless connections.

                        The internet backbone, consisting of high-speed networks, connects major hubs and data centers, facilitating long-distance data transfer. Intermediary devices, such as switches and routers, direct packets along the optimal path.

                        At the destination, packets are reassembled to reconstruct the original data. During the transfer, acknowledgments are sent back to confirm successful receipt, and error-checking mechanisms request retransmission for any lost or corrupted packets.

                        TCP/IP is the foundational protocol suite for internet communication, ensuring reliable and orderly data delivery. This dynamic process enables users to access websites, send emails, and interact across the internet, making it essential for our interconnected world.'''
    )


    Example16 = InputOutputTextPair(
        input_text="Protocol in network layer ",
        output_text='''In the network layer of the OSI (Open Systems Interconnection) model and the Internet layer of the TCP/IP model, there are several key protocols that play essential roles in routing and forwarding data packets across networks. These protocols facilitate the delivery of data to their intended destinations. Some of the most notable protocols in the network layer are:

                        Internet Protocol (IP): The Internet Protocol (IP) is the fundamental protocol of the network layer. It provides the addressing scheme and routing mechanisms to deliver data packets across interconnected networks, ensuring data reaches its destination.

                        Internet Control Message Protocol (ICMP): ICMP is used for error reporting, diagnostics, and management of network devices. It is often used to check the availability and responsiveness of network hosts through tools like ping.

                        Internet Group Management Protocol (IGMP): IGMP is used to manage multicast group membership. It allows devices to join and leave multicast groups to receive specific data streams efficiently.

                        Routing Information Protocol (RIP): RIP is a distance-vector routing protocol that helps routers exchange routing information and determine the best paths for forwarding packets.

                        Open Shortest Path First (OSPF): OSPF is a link-state routing protocol that calculates the shortest path to each network by considering the link's cost. It is widely used in large-scale networks.

                        Border Gateway Protocol (BGP): BGP is a path-vector routing protocol used for exchanging routing information between autonomous systems (AS). It is the primary protocol that enables communication between different internet service providers (ISPs).

                        Enhanced Interior Gateway Routing Protocol (EIGRP): EIGRP is a Cisco proprietary routing protocol designed to efficiently exchange routing information and reduce convergence time in a network.

                        These protocols work together to ensure efficient and reliable data transmission in computer networks. IP, being the core protocol of the network layer, plays a central role in determining the route that data packets take from the source to the destination. Other protocols, like ICMP, assist in network troubleshooting and diagnostics. The combination of these protocols enables data to navigate through complex networks and reach its intended recipients.'''
    )

    Example17 = InputOutputTextPair(
        input_text="Transport layer protocols",
        output_text='''In the transport layer of the OSI (Open Systems Interconnection) model and the transport layer of the TCP/IP model, there are two primary protocols that are commonly used:

                        Transmission Control Protocol (TCP): TCP is a connection-oriented protocol that ensures reliable data delivery between applications. It establishes a connection between the sender and receiver before data transfer, and it guarantees that data packets are delivered in the correct order without loss or duplication. TCP also handles flow control, ensuring that data is sent at a rate suitable for the receiver's capacity to process it. It is widely used for applications that require error-free and ordered data transmission, such as web browsing, file transfers, and email.

                        User Datagram Protocol (UDP): UDP is a connectionless protocol that provides a lightweight, fast, and simple method for sending datagrams (packets) from one host to another. Unlike TCP, UDP does not establish a connection before data transfer and does not guarantee reliable delivery or packet ordering. As a result, UDP is considered less reliable than TCP but is preferred for real-time applications like audio and video streaming, online gaming, and VoIP (Voice over Internet Protocol). These applications can tolerate some data loss and are more concerned with minimizing latency.

                        Both TCP and UDP serve distinct purposes and are used based on the specific requirements of the applications they support. TCP is ideal for applications that prioritize data integrity and accuracy, while UDP is suitable for applications where low latency and speed are essential, and some data loss can be tolerated.'''
    )

    if request.method == "POST":
        usr = request.form.get("userinput2")
        response = chat2.send_message(usr, **parameters)
        return jsonify({"response": response})
    else:
        return render_template("chatbot2.html")

@app.route("/getsgurl")
def getgirl():
    return render_template("getsgurl.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
