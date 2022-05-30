<!-- PROJECT LOGO -->
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
  </a>

  <h3 align="center">Text classifier with Flask and  🤗 transformers library</h3>
</div>

<br />
<p align="center">
  <img src="https://github.com/vocdex/text-summarizer/blob/main/text-summarizer.gif" width="650" title="hover text">
</p>

<!-- ABOUT THE PROJECT -->
## About The Project
It's a simple web app that I created from scratch to practice my Flask and NLP skills. The app receives a text input and returns 
maximum length of 64 character summary.  
I made use of HuggingFace pipeline by downloading the checkpoint, DistillBart which is a distilled version of BART.
BART is a sequence-to-sequence model trained as a denoising autoencoder.  
Distilled BART is a distilled version of BART that keeps up 97% of BART performance while reducing the model size by 40%.



<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [HuggingFace](https://huggingface.co/)
* [Semantic UI](https://semantic-ui.com/)
* [Flask](https://flask.palletsprojects.com/en/2.1.x/)
* [Pytorch](https://pytorch.org/)
<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage
```
git clone https://github.com/vocdex/text-summarizer.git
pip install -r requirements.txt
```
```
export FLASK_APP=app.py
flask run
```
## Issues
Even though a lighter distilled version of the model is used, it is still large(~423MB)and takes a while to download and cache the model when the user runs the app for the first time.












