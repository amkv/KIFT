// fork getUserMedia for multiple browser versions, for the future
// when more browsers support MediaRecorder

navigator.getUserMedia = ( navigator.getUserMedia ||
                       navigator.webkitGetUserMedia ||
                       navigator.mozGetUserMedia ||
                       navigator.msGetUserMedia);

// set up basic variables for app

var record = document.querySelector('.record');
var stop = document.querySelector('.stop');
var soundClips = document.querySelector('.sound-clips');
var canvas = document.querySelector('.visualizer');

// disable stop button while not recording

stop.disabled = true;

// visualiser setup - create web audio api context and canvas

var audioCtx = new (window.AudioContext || webkitAudioContext)();
var canvasCtx = canvas.getContext("2d");

//main block for doing the audio recording

if (navigator.getUserMedia) {
  console.log('getUserMedia supported.');

  var constraints = { audio: true };
  var chunks = [];

  var onSuccess = function(stream) {
    var mediaRecorder = new MediaRecorder(stream);

    // Visualizer
    visualize(stream);

    record.onclick = function() {
      mediaRecorder.start();
      console.log(mediaRecorder.state);
      console.log("recorder started");
      record.style.background = "red";

      stop.disabled = false;
      record.disabled = true;
    }

    stop.onclick = function() {
      // Stop recording
      mediaRecorder.stop();
      console.log(mediaRecorder.state);
      console.log("recorder stopped");
      record.style.background = "";
      record.style.color = "";
      // mediaRecorder.requestData();

      stop.disabled = true;
      record.disabled = false;
    }

    // The MediaRecorder.onstop event handler (part of the MediaRecorder API)
    // handles the stop event, allowing you to run code in response to media
    // recording via a MediaRecorder being stopped.
    mediaRecorder.onstop = function(e) {
      console.log("data available after MediaRecorder.stop() called.");

      // var clipName = "Audio File";
      // console.log(clipName);
      var clipContainer = document.createElement('article');
      // var clipLabel = document.createElement('p');
      // var audio = document.createElement('audio');
      // var audio2upload = document.createElement('input');
      // var deleteButton = document.createElement('button');
      var callBack = document.createElement('p');

      // Create form that will be sent
      // var upload_form = document.createElement('form');
      // upload_form.setAttribute('method','post');
      // upload_form.setAttribute('action',"http://127.0.0.1:8081/submit");

      // var submit = document.createElement("input"); //input element, Submit button
      // submit.setAttribute('type',"submit");
      // submit.setAttribute('value',"Submit");
      // audio2upload.setAttribute('controls', '');

      // upload_form.appendChild(audio2upload);
      // upload_form.appendChild(submit);
      // End form

      // clipContainer.classList.add('clip');
      // audio.setAttribute('controls', '');
      // deleteButton.textContent = 'Delete';
      // deleteButton.className = 'delete';

      // if(clipName === null) {
      //   clipLabel.textContent = 'My unnamed clip';
      // } else {
      //   clipLabel.textContent = clipName;
      // }

      callBack.innerHTML = 'Upload OK';

      // clipContainer.appendChild(audio);
      // clipContainer.appendChild(clipLabel);
      // clipContainer.appendChild(deleteButton);
      // clipContainer.appendChild(upload_form);
      clipContainer.appendChild(callBack);
      soundClips.appendChild(clipContainer);

      // audio.controls = true;
      var blob = new Blob(chunks, {'type': 'audio/x-wav;'});
      console.log(blob.type);
      chunks = [];
      console.log(window.URL.createObjectURL(blob));
      // var audioURL = window.URL.createObjectURL(blob);
      // audio.src = audioURL;
      // audio2upload.value = audioURL;
      console.log("recorder stopped");

      // deleteButton.onclick = function(e) {
      //   evtTgt = e.target;
      //   evtTgt.parentNode.parentNode.removeChild(evtTgt.parentNode);
      // }

      // When everything is done, send the file to the server
      sendAudio(blob);

    }
    // The MediaRecorder.ondataavailable event handler (part of the MediaStream
    // Recording API) handles the dataavailable event, letting you run code in
    // response to Blob data being made available for use.
    mediaRecorder.ondataavailable = function(e) {
      chunks.push(e.data);
    }
  }

  var onError = function(err) {
    console.log('The following error occured: ' + err);
  }

  navigator.getUserMedia(constraints, onSuccess, onError);
} else {
   console.log('getUserMedia not supported on your browser!');
}


// Function to sendAudio
function sendAudio(blob) {
    // var myHeaders = new Headers();
    // myHeaders.append("Content-Type", "audio/x-wav");

    fetch("http://127.0.0.1:8081/submit", {
    method: "post",
    headers: new Headers({
      "Content-Type": "image/png"
    }),
    body: blob
    });
  // console.log(myHeaders);
  console.log("end_fetch");
}


// Nice to have, voice visualisation
function visualize(stream) {
  var source = audioCtx.createMediaStreamSource(stream);

  var analyser = audioCtx.createAnalyser();
  analyser.fftSize = 2048;
  var bufferLength = analyser.frequencyBinCount;
  var dataArray = new Uint8Array(bufferLength);

  source.connect(analyser);
  //analyser.connect(audioCtx.destination);

  WIDTH = canvas.width
  HEIGHT = canvas.height;

  draw()

  function draw() {

    requestAnimationFrame(draw);

    analyser.getByteTimeDomainData(dataArray);

    canvasCtx.fillStyle = 'rgb(200, 200, 200)';
    canvasCtx.fillRect(0, 0, WIDTH, HEIGHT);

    canvasCtx.lineWidth = 2;
    canvasCtx.strokeStyle = 'rgb(0, 0, 0)';

    canvasCtx.beginPath();

    var sliceWidth = WIDTH * 1.0 / bufferLength;
    var x = 0;


    for(var i = 0; i < bufferLength; i++) {

      var v = dataArray[i] / 128.0;
      var y = v * HEIGHT/2;

      if(i === 0) {
        canvasCtx.moveTo(x, y);
      } else {
        canvasCtx.lineTo(x, y);
      }

      x += sliceWidth;
    }

    canvasCtx.lineTo(canvas.width, canvas.height/2);
    canvasCtx.stroke();

  }
}
