# Problem Identification and Risk Analysis?

An Efficient and secured delivery management System. In our idea, there is some risk like RFID costly in some case, in Cash by code customer have to pay through a gateway which will make some issue sometime.

## Idea formulation
• Stealing Packages
o Tracking Package in every step with RFID
• Stealing Collected cash of COD
o Online Payment through cash by code after delivery
• Delivery boy un-attend next day without notice.
o Other delivery boys will be assigned by the algorithm.
## Implementation plan and Work progress
To prevent stealing packages, we will use will generate an RFID tag and will sync it to with our system by which we can track every single product in each step efficiently, and no one will able to move any package without dispatching from the system it will minimize the risk of stealing a product.
To prevent stealing collected cash of COD, we will use the Cash by Code option where the customer will generate a code for a limited time by making a pending payment request which will be accomplished by forwarding the code to the delivery man. The delivery man will update the code to the server which will be a confirmation of product delivery accomplishment as well as a cash transaction.
To prevent the problem regarding un attend a delivery boy without notice, we will imply an algorithm. This algorithm will assign the scheduled task of the unattended delivery boy to the available delivery boy. This algorithm will take two attributes like the available time of delivery boy and the distance between two places of the assigned and unassigned tasks. The system will measure the time to move between these two places and based on the available time of delivery boy system will measure. After finishing for the lowest distance and it will work for the second-lowest distance.
