#include <nan.h>
#include <iostream>
#include "cryptonight/cryptonight.h"

using namespace Nan;
using namespace v8;

NAN_METHOD(cryptonote_hash) {
	char* inputData = (char*) node::Buffer::Data(info[0]);
	unsigned int size = info[0]->Uint32Value();
	char * output = new char[32];
	
	cryptonight(output, inputData, size);

 	info.GetReturnValue().Set(Nan::CopyBuffer(output, 32).ToLocalChecked());
}

NAN_MODULE_INIT(Init) {
   Nan::Set(target, New<String>("cryptonote_hash").ToLocalChecked(),
        GetFunction(New<FunctionTemplate>(cryptonote_hash)).ToLocalChecked());
}

NODE_MODULE(buffer_example, Init)