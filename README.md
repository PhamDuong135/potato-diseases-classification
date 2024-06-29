## Set up for Python
1. Install Python: ([Download](https://www.python.org))

2. Install Python packages:
```
pip3 install -r training/requirements.txt
pip3 install -r api/requirements.txt
```
## Set up for ReactJS
1. Install Nodejs ([Download](https://nodejs.org/en/download/package-manager/))
2. Install NPM
3. Install Dependencies
```bash
cd frontend
npm install
npm audit fix
```

4. Copy `.env.example` as `.env`.
5. Change API url in `.env`.

## Training Model
1. Download the data from [kaggle](https://www.kaggle.com/arjuntejaswi/plant-village).
2. Only keep folders related to Potatoes.
3. Run Jupyter Notebook in Browser.

```bash
jupyter notebook
```
4. Open `training/potato-disease-training.ipynb` in Jupyter Notebook.
5. In cell #2, update the path to dataset.
6. Run all the Cells one by one.
7. Copy the model generated and save it with the version number in the `saved_models` folder.

## Running the API

### Using FastAPI
1. Get inside `api` folder
```bash
cd api
```
2. Start main.py file to run the FastAPI Server using uvicorn
```bash
python main.py
```
3. Your API is now running at `localhost:8000`

## Running the Frontend
1. Get inside `api` folder
```bash
cd frontend
```
2. Update .env file: `REACT_APP_API_URL` to API URL if needed.
3. Run the frontend
```bash
npm run start
```

