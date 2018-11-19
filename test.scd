(
x = CSVFileReader.readInterpret("C:\\Users\\Aditya Adhikary\\Desktop\\DA\\DA Proj\\Project\\testData.csv").postcs.flat;
)

(
 SynthDef(\example8, {|out = 0, freq, amp, dur, pan = 0|

  var pm, modulator, env, panner;

  modulator = SinOsc.ar(50, 0, 0.2);
  pm = SinOsc.ar(freq, modulator);

  env = EnvGen.kr(Env.perc(0.01, dur, amp), doneAction:2);
  panner = Pan2.ar(pm, pan, env);

  Out.ar(out, panner);
 }).store
)


(
  ~func = { arg ratio_arr, baseFreq = 440, detune = 10, dur  = 0.2;
   ~t = Task({
   var freq;

   ratio_arr.do({ |ratio, index|
    freq =  (ratio * baseFreq) + detune;
    Synth(\example8, [\out, 0, \freq, freq, \amp, 0.2, \dur, dur,
       \pan, 0]);
    dur.wait;
   });
  });
 };

 ~arr = x;

 ~func.value(~arr, 440, 1, 0.001).play;

)

~t.pause;
~t.resume;
~t.play;

~func.value(~arr, 440, 1, 0.001).play;
~func.value(~arr, 440, 1, 0.1).play;

~func.value(~arr, 440, 1, 0.001).play;

(
w = Window("mySynth",500@500);
w.front;


EZKnob(w,Rect(10,20,100,100),"basefreq",ControlSpec(100,500)).action = {|slider| ~func.value.set(\baseFreq,slider.value.postln)};

EZKnob(w,Rect(120,20,100,100),"detune",ControlSpec(1,10)).action = {|slider| ~func.value.set(\detune,slider.value.postln)};

EZKnob(w,Rect(230,20,100,100),"dur",ControlSpec(0.01,10)).action = {|slider| ~func.value.set(\dur,slider.value.postln)};

)

// (
// w = Window("Playing a sequence of images",500@500);
// w.front;
//
//
// //EZSlider(w,Rect(10,10,300,20),"freq").action_({|slider| ~mySynth.set(\freq, (100 + (slider.value * 400).postln) ) });
//
// EZSlider(w,Rect(10,10,300,20),"basefreq",ControlSpec(100,500)).action = {|slider| ~func.value.set(\baseFreq,slider.value.postln)}; // warp could also be \lin
//
//
// EZSlider(w,Rect(10,40,300,20),"detune",ControlSpec(100,500)).action = {|slider| ~func.value.set(\detune,slider.value.postln)};
//
// EZSlider(w,Rect(10,700,300,20),"detune",ControlSpec(100,500)).action = {|slider| ~func.value.set(\detune,slider.value.postln)});
//
//
// )
