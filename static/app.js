var audio_context;
var recorder;
var record = document.querySelector('.record');
var stop = document.querySelector('.stop');

function startUserMedia(stream) {
  var input = audio_context.createMediaStreamSource(stream);
  console.log('Media stream created.');

  recorder = new Recorder(input);
  console.log('Recorder initialised.');
}

function startRecording(button) {
  recorder && recorder.record();
  record.style.background = "red";
  button.disabled = true;
  button.nextElementSibling.disabled = false;
  console.log('Recording...');
}

function stopRecording(button) {
  recorder && recorder.stop();
  button.disabled = true;
  button.previousElementSibling.disabled = false;
  record.style.background = "";
  record.style.color = "";
  // mediaRecorder.requestData();

  stop.disabled = true;
  record.disabled = false;
  console.log('Stopped recording.');

  POSTAudioRequest();
  recorder.clear();
}

function POSTAudioRequest() {
  recorder && recorder.exportWAV(function(blob) {
    fetch("http://127.0.0.1:8081/submit", {
    method: "post",
    body: blob
    });
  console.log("end_fetch");
  });
}

window.onload = function init() {
  try {
    // webkit shim
    window.AudioContext = window.AudioContext || window.webkitAudioContext;
    navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia;
    window.URL = window.URL || window.webkitURL;

    audio_context = new AudioContext;
    console.log('Audio context set up.');
    console.log('navigator.getUserMedia ' + (navigator.getUserMedia ? 'available.' : 'not present!'));
  } catch (e) {
    alert('No web audio support in this browser!');
  }

  navigator.getUserMedia({audio: true}, startUserMedia, function(e) {
    console.log('No live audio input: ' + e);
  });
};
