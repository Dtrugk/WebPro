from google.cloud import aiplatform
from vertexai.preview.language_models import ChatModel, InputOutputTextPair,ChatSession


def chat(usr:str):
    chat_model = ChatModel.from_pretrained("chat-bison@001")
    chat = ChatSession(chat_model)

    # TODO developer - override these parameters as needed:
    parameters = {
        "temperature": 0.5,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 1000,  # Token limit determines the maximum amount of text output.
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

Marketing and Distribution: Once the car is ready for the market, marketing and distribution strategies are put in place to make it available to consumers.

It's important to note that building a car is a complex and capital-intensive process that is typically undertaken by established automakers or specialized companies. Attempting to build a car from scratch as an individual is not practical or safe. If you are interested in automobiles and engineering, consider exploring careers in automotive design, engineering, or manufacturing.'''
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

    Example15 = InputOutputTextPair(
        input_text="Comapre OSI model and TCP/IP model ",
        output_text='''The OSI (Open Systems Interconnection) model and the TCP/IP model are both conceptual frameworks used to understand and standardize the communication protocols used in computer networks. They provide a structured way of categorizing and explaining the various layers of network communication. Let's briefly explore each model:

                        OSI Model (Open Systems Interconnection Model):
                        The OSI model is a theoretical framework developed by the International Organization for Standardization (ISO) to facilitate communication between different systems and network devices. It consists of seven layers, each responsible for specific tasks in the process of data communication:

                        Physical Layer: Deals with the physical transmission of data over the network medium, such as cables or wireless signals.

                        Data Link Layer: Handles the reliable transmission of data frames between directly connected devices and provides error detection and correction.

                        Network Layer: Manages the routing of data packets between different networks, ensuring data reaches its intended destination.

                        Transport Layer: Ensures reliable end-to-end communication by segmenting data, handling flow control, and providing error recovery through protocols like TCP (Transmission Control Protocol) or UDP (User Datagram Protocol).

                        Session Layer: Manages the establishment, maintenance, and termination of sessions between applications.

                        Presentation Layer: Translates data into a format that can be understood by the application layer, handling data encryption, compression, and decryption.

                        Application Layer: Provides a user interface and network services for applications to access network resources.

                        TCP/IP Model (Transmission Control Protocol/Internet Protocol Model):

                        The TCP/IP model is a more practical and widely used model, based on the protocols that actually make up the internet's communication system. It consists of four layers:

                        Application Layer: Corresponds to the application layer of the OSI model, providing network services directly to applications.

                        Transport Layer: Corresponds to both the transport and session layers of the OSI model. It ensures reliable end-to-end communication and supports both TCP (reliable, connection-oriented) and UDP (unreliable, connectionless) protocols.

                        Internet Layer: Corresponds to the network layer of the OSI model, handling the routing of data packets across different networks. It is mainly associated with the IP (Internet Protocol).

                        Link Layer: Combines the data link and physical layers of the OSI model, dealing with the actual transmission of data over the physical network medium.

                        The TCP/IP model is widely used in modern networks, especially the internet, and has become the de facto standard for network communication.

                        In summary, the OSI model is a theoretical reference model with seven layers, while the TCP/IP model is a practical model with four layers, representing the protocols used in the real-world implementation of computer networks and the internet. Both models provide a structured approach to understanding network communication.'''
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

    response = chat.send_message(
        usr, **parameters
    )

    return response

