#!/bin/bash

export PYTHONPATH=$(pwd)/backend

echo "🐍 Python: $(which python)"
echo "📦 Pip: $(which pip)"
echo "🔗 PYTHONPATH: $PYTHONPATH"

python -c "import pymongo; print('✅ pymongo:', pymongo.__version__)" || echo "❌ pymongo not found"
python -c "import redis; print('✅ redis:', redis.__version__)" || echo "❌ redis not found"
python -c "from services.summary import blending_service; print('✅ PYTHONPATH is working')" || echo "❌ PYTHONPATH issue"
