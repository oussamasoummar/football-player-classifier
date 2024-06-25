## Football Player Classifier

This project involves building a web application for classifying football players between Messi, Ronaldo, and Mbappe. The project workflow includes:

- **Data Collection and Cleaning:**

  - Data is collected from various web sources and cleaned for consistency.
  - used opencv for keeping just the images that have two eyes.
  
- **Image Processing with PyWavelet:**

  - Utilizes PyWavelet, an image processing technique, to extract crucial features from images that are essential for training the machine learning models.
  
- **Model Selection:** Experimentation with multiple models resulted in identifying the SVM (Support Vector Machine) model as delivering the best accuracy and performance.
  
- **Web Application Development:** Implemented using Flask for the backend and HTML, CSS, and JavaScript for the frontend to provide a user-friendly interface.
  
- **Functionality:** Users can upload images of football players, and the application will classify them into one of the three categories based on the trained SVM model.
  <img width="954" alt="Screenshot 2024-06-25 210917" src="https://github.com/oussamasoummar/football-player-classifier/assets/125143323/1c5d734b-9a2b-44e3-94b1-7f00d4ecc04f">
  <img width="960" alt="after_classifier" src="https://github.com/oussamasoummar/football-player-classifier/assets/125143323/bd3baacb-def4-4b57-9e68-91d44ac13d75">
- **technologies:**
  


