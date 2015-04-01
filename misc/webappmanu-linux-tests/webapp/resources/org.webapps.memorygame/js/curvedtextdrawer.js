CurvedTextDrawer=function(a){function b(a,b,c){var d=new Vec2(0,-c);return d.rotate(a),d.add(b),d}return console.log("--> new CurvedTextDrawer()"),this.canvasElem=a,this.backgroundFill="",this.useFont="30px Arial",this.textColor="black",this.getCanvasCenterPos=function(){return new Vec2(this.canvasElem.width/2,this.canvasElem.height/2)},this.clearCanvas=function(){var a=this.canvasElem.getContext("2d");this.backgroundFill.length>0&&(a.fillStyle=this.backgroundFill,a.fillRect(0,0,this.canvasElem.width,this.canvasElem.height))},this.drawSectorArc=function(a,c,d,e,f,g,h,i,j){console.log("--> CurvedTextDrawer.drawSectorArc()");var k=this.canvasElem.getContext("2d");this.clearCanvas(),k.textBaseline="middle",k.textAlign="center",k.font=this.useFont,k.fillStyle=this.textColor;var l=0;"cw"==h?l=1:"ccw"==h&&(l=-1);var m=degs2Rads(g),n=k.measureText(a).width,o=0,p=degs2Rads(f);if(console.log("    align: "+j),"left"==j){var q=m*Math.PI*e/Math.PI;o=m/q}else if("right"==j){var q=m*Math.PI*e/Math.PI;o=m/q,p=clampRotationValue(p+m-n*o,"rads")}else if("center"==j){var q=m*Math.PI*e/Math.PI;o=m/q;var r=k.measureText(a[0]).width/2;r+=k.measureText(a[a.length-1]).width/2,p=clampRotationValue(p+(n-r)/2*o,"rads")}else"justify"==j&&(o=degs2Rads(g)/n);for(var s=new Vec2(c,d),t=0;t<a.length;++t){var u=a[t],v=b(p,s,e);k.save(),k.translate(v.mX,v.mY),k.rotate(i?p+Math.PI:p),k.fillText(u,0,0),k.restore();var w=k.measureText(u).width/2;t+1<a.length&&(w+=k.measureText(a[t+1]).width/2),console.log("    char: "+u+", w:"+w+", angle: "+w*o*l),p+=w*o*l,p>=2*Math.PI&&(p-=2*Math.PI),0>p&&(p+=2*Math.PI)}console.log("<-- CurvedTextDrawer.drawSectorArc()")},this};