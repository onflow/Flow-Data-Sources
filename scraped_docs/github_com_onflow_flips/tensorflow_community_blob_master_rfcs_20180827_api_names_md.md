# Source: https://github.com/tensorflow/community/blob/master/rfcs/20180827-api-names.md

# TensorFlow Namespaces

| Status        | Accepted       |
:-------------- |:---------------------------------------------------- |
| **Author(s)** | Anna Revinskaya (annarev@google.com), Andrew Selle (aselle@google.com) |
| **Sponsor**   | Martin Wicke (wicke@google.com)                      |
| **Updated**   | 2018-08-27                                           |

## Objective

This document proposes organizing TensorFlow API symbols in corresponding logical subnamespaces. As TensorFlow library grows, it is important to structure namespaces in a clear way for easier discoverability and usability.

We define **endpoint** as full name that can be used to access a TensorFlow
symbol. For e.g.
[name_scope](https://www.tensorflow.org/api_docs/python/tf/name_scope) can be
accessed using either `tf.name_scope` or  `tf.keras.backend.name_scope`.
Therefore, `name_scope` has 2 endpoints: `tf.name_scope` and
`tf.keras.backend.name_scope`.

At a high level we have the following goals:

*   Add a few additional namespaces.
*   Add additional endpoints for TensorFlow symbols in relevant namespaces.
*   Remove some of the existing endpoints.

## Motivation

TensorFlow currently has over 2000 endpoints total including over 500 endpoints in the root namespace. As number of symbols grows, it is important to maintain a clear structure to aid discoverability.

Certain API symbol placements could be improved:

*   Some namespaces were created recently and might not contain all the
    corresponding symbols. For e.g. `tf.math` namespace was added recently.
    Symbols such as `tf.round` are not in `tf.math` namespace even though logically they belong in that namespace.
*   Some symbols are included in the root namespace even though they are rarely
    used (for e.g. `tf.zeta`).
*   Some symbols currently start with a prefix that could really be replaced by
    introducing a subnamespace (for e.g. `tf.string_strip` vs
    `tf.strings.strip`, `tf.sparse_maximum` vs `tf.sparse.maximum`).
*   Certain deep hierarchies seem redundant and could be flattened (for e.g.
    `tf.saved_model.signature_constants.CLASSIFY_INPUTS` could be moved to
    `tf.saved_model.CLASSIFY_INPUTS`).
*   To keep clear structure and reduce duplication, we want to collect all layers, losses and metrics under the `tf.keras` namespace.

In general, we want to balance flatness and browsability. Flat hierarchies allow
for shorter endpoint names that are easy to remember (for e.g. `tf.add` vs
`tf.math.add`). At the same time subnamespaces support easier browsability (for
e.g. `tf.math` namespace would contain all math functions making it easier to discover available symbols).

Furthermore, TensorFlow API has many users. Therefore, we should avoid removing endpoints if they are frequently used.

## Design Proposal

## Additional namespaces

We plan to add the following additional namespaces:

**tf.random** - will contain random sampling ops.  
**tf.keras.layers** - will contain all symbols that are currently under `tf.layers`. Note that signatures of these symbols will likely change to match layers under tf.keras.layers better.  
**tf.keras.losses** - will contain all symbols that are currently under `tf.losses`. Note that signatures of these symbols will likely change to match losses under tf.keras.losses better.  
**tf.keras.metrics** - will contain all symbols that are currently under `tf.metrics`. Note that signatures of these symbols will likely change to match metrics under tf.keras.metrics better.  


Note that we already introduced some new namespaces earlier in June, specifically

**tf.debugging** - ops helpful for debugging, such as asserts. We also want to
move [TensorFlow Debugger](https://www.tensorflow.org/guide/debugger) to
`tf.debugging` namespace.

**tf.dtypes** - data types.

**tf.io** - ops for reading and writing.

**tf.quantization** - ops related to quantization.

## Deprecated namespaces

We plan to deprecate entire contents of the following namespaces:

**tf.logging** - Python `logging` module can be used instead.  
**tf.manip** - We will keep endpoints in root for symbols in `tf.manip`. `tf.manip` was added recently but most tensor manipulation ops are frequently used and it makes sense to keep them in root instead.  


## Additional endpoints

We will add new endpoints for existing symbols to make sure each namespace contains all relevant endpoints.

See list of endpoints we want to add in *Appendix 1: Additional
Endpoints*. Note: the list in the appendix does not include new endpoints for symbols under
`tf.layers`, `tf.losses` and `tf.metrics` namespaces since all symbols under
these namespaces will have new endpoints added under `tf.keras.layers`,
`tf.keras.losses` and `tf.keras.metrics` respectively. So, we don't need to
list these endpoint changes individually.


## Deprecated endpoints

We also want to remove some of the existing endpoints. Specifically we were looking for endpoints to remove based on the following criteria:

*   Remove endpoints if they have preferred replacement and if these endpoints are not frequently used.
*   Remove all endpoints that have been moved to `tf.quantization` namespace.
*   Remove all endpoints that have been moved to `tf.random` namespace.
*   Remove all endpoints from `tf.logging`.

In total, we propose to remove 214 endpoints, including 171 endpoints in the root namespace.

See the list of endpoints we want to remove in *Appendix 2: Deprecated
Endpoints*. Note: the list in the appendix does not include endpoints under `tf.logging` since entire contents of this module will be deprecated. So, we don't need to list these endpoints individually.


# Impact

Browsing for symbols should become easier. For e.g. page for `tf.math` namespace should display all math functions that TensorFlow provides. Similarly, `tf.sets` namespace page should display all available set operations.

Removing symbol endpoints would break references in user code. We plan to apply removals as a part of TensorFlow 2.0 release and provide a conversion script that would replace deprecated references with canonical ones. Initial script is at https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/compatibility/tf_upgrade_v2.py. It will be updated to match changes in this doc.


# Work Estimates

Work will be done in multiple stages:



1.  We will first add new endpoints. I have some changes ready, so this step should take 1-2 weeks.
1.  Second step is to remove deprecated endpoints. This will be done later as a part of TensorFlow 2.0 release. Removing endpoints will take about 2 weeks.


# Appendix 1: Additional Endpoints

In addition to symbols in this table, we plan to add all symbols under
`tf.layers`, `tf.losses`, `tf.metrics` to `tf.keras.layers`, `tf.keras.losses`,
`tf.keras.metrics` respectively.

| Current name  | New names |
:-------------- |:---------------------------------------------------- |
| tf.Assert | tf.debugging.Assert |
| tf.COMPILER_VERSION | tf.version.COMPILER_VERSION |
| tf.CXX11_ABI_FLAG | tf.sysconfig.CXX11_ABI_FLAG |
| tf.DType | tf.dtypes.DType |
| tf.FixedLenFeature | tf.io.FixedLenFeature |
| tf.FixedLenSequenceFeature | tf.io.FixedLenSequenceFeature |
| tf.GIT_VERSION | tf.version.GIT_VERSION |
| tf.GRAPH_DEF_VERSION | tf.version.GRAPH_DEF_VERSION |
| tf.GRAPH_DEF_VERSION_MIN_CONSUMER | tf.version.GRAPH_DEF_VERSION_MIN_CONSUMER |
| tf.GRAPH_DEF_VERSION_MIN_PRODUCER | tf.version.GRAPH_DEF_VERSION_MIN_PRODUCER |
| tf.HistogramProto | tf.summary.HistogramProto |
| tf.MONOLITHIC_BUILD | tf.sysconfig.MONOLITHIC_BUILD |
| tf.PaddingFIFOQueue | tf.io.PaddingFIFOQueue |
| tf.Print | tf.debugging.Print |
| tf.PriorityQueue | tf.io.PriorityQueue |
| tf.QUANTIZED_DTYPES | tf.dtypes.QUANTIZED_DTYPES |
| tf.QueueBase | tf.io.QueueBase |
| tf.RandomShuffleQueue | tf.io.RandomShuffleQueue |
| tf.SparseConditionalAccumulator | tf.sparse.SparseConditionalAccumulator |
| tf.SparseFeature | tf.io.SparseFeature |
| tf.SparseTensor | tf.sparse.SparseTensor |
| tf.SparseTensorValue | tf.sparse.SparseTensorValue |
| tf.SummaryMetadata | tf.summary.SummaryMetadata |
| tf.VERSION | tf.version.VERSION |
| tf.VarLenFeature | tf.io.VarLenFeature |
| tf.abs | tf.math.abs |
| tf.accumulate_n | tf.math.accumulate_n |
| tf.add_n | tf.math.add_n |
| tf.angle | tf.math.angle |
| tf.argmax | tf.math.argmax |
| tf.argmin | tf.math.argmin |
| tf.as_dtype | tf.dtypes.as_dtype |
| tf.assert_equal | tf.debugging.assert_equal |
| tf.assert_greater | tf.debugging.assert_greater |
| tf.assert_greater_equal | tf.debugging.assert_greater_equal |
| tf.assert_integer | tf.debugging.assert_integer |
| tf.assert_less | tf.debugging.assert_less |
| tf.assert_less_equal | tf.debugging.assert_less_equal |
| tf.assert_near | tf.debugging.assert_near |
| tf.assert_negative | tf.debugging.assert_negative |
| tf.assert_non_negative | tf.debugging.assert_non_negative |
| tf.assert_non_positive | tf.debugging.assert_non_positive |
| tf.assert_none_equal | tf.debugging.assert_none_equal |
| tf.assert_positive | tf.debugging.assert_positive |
| tf.assert_proper_iterable | tf.debugging.assert_proper_iterable |
| tf.assert_rank | tf.debugging.assert_rank |
| tf.assert_rank_at_least | tf.debugging.assert_rank_at_least |
| tf.assert_rank_in | tf.debugging.assert_rank_in |
| tf.assert_same_float_dtype | tf.debugging.assert_same_float_dtype |
| tf.assert_scalar | tf.debugging.assert_scalar |
| tf.assert_type | tf.debugging.assert_type |
| tf.bfloat16 | tf.dtypes.bfloat16 |
| tf.bitcast | tf.dtypes.bitcast |
| tf.bincount | tf.math.bincount |
| tf.bool | tf.dtypes.bool |
| tf.cast | tf.dtypes.cast |
| tf.complex | tf.dtypes.complex |
| tf.complex128 | tf.dtypes.complex128 |
| tf.complex64 | tf.dtypes.complex64 |
| tf.confusion_matrix | tf.train.confusion_matrix |
| tf.conj | tf.math.conj |
| tf.count_nonzero | tf.math.count_nonzero |
| tf.cumprod | tf.math.cumprod |
| tf.cumsum | tf.math.cumsum |
| tf.decode_csv | tf.io.decode_csv |
| tf.depth_to_space | tf.nn.depth_to_space |
| tf.deserialize_many_sparse | tf.io.deserialize_many_sparse |
| tf.divide | tf.math.divide |
| tf.double | tf.dtypes.double |
| tf.erf | tf.math.erf |
| tf.float16 | tf.dtypes.float16 |
| tf.float32 | tf.dtypes.float32 |
| tf.float64 | tf.dtypes.float64 |
| tf.floordiv | tf.math.floordiv |
| tf.floormod | tf.math.floormod |
| tf.get_seed | tf.random.get_seed |
| tf.global_norm | tf.linalg.global_norm |
| tf.half | tf.dtypes.half |
| tf.imag | tf.math.imag |
| tf.import_graph_def | tf.graph_util.import_graph_def |
| tf.int16 | tf.dtypes.int16 |
| tf.int32 | tf.dtypes.int32 |
| tf.int64 | tf.dtypes.int64 |
| tf.int8 | tf.dtypes.int8 |
| tf.is_non_decreasing | tf.debugging.is_non_decreasing |
| tf.is_numeric_tensor | tf.debugging.is_numeric_tensor |
| tf.is_strictly_increasing | tf.debugging.is_strictly_increasing |
| tf.lbeta | tf.math.lbeta |
| tf.log_sigmoid | tf.math.log_sigmoid |
| tf.logical_xor | tf.math.logical_xor |
| tf.manip.roll | tf.roll |
| tf.matmul | tf.linalg.matmul |
| tf.mod | tf.math.mod |
| tf.multinomial | tf.random.multinomial |
| tf.multiply | tf.math.multiply |
| tf.negative | tf.math.negative |
| tf.nn.in_top_k | tf.math.in_top_k |
| tf.nn.l2_normalize | tf.math.l2_normalize, tf.linalg.l2_normalize |
| tf.nn.log_softmax | tf.math.log_softmax |
| tf.nn.log_uniform_candidate_sampler | tf.random.log_uniform_candidate_sampler |
| tf.nn.sigmoid | tf.math.sigmoid |
| tf.nn.softmax | tf.math.softmax |
| tf.nn.top_k | tf.math.top_k |
| tf.nn.uniform_candidate_sampler | tf.random.uniform_candidate_sampler |
| tf.nn.zero_fraction | tf.math.zero_fraction |
| tf.parse_example | tf.io.parse_example |
| tf.parse_single_example | tf.io.parse_single_example |
| tf.parse_single_sequence_example | tf.io.parse_single_sequence_example |
| tf.pow | tf.math.pow |
| tf.python_io.TFRecordCompressionType | tf.io.TFRecordCompressionType |
| tf.python_io.TFRecordOptions | tf.io.TFRecordOptions |
| tf.python_io.TFRecordWriter | tf.io.TFRecordWriter |
| tf.python_io.tf_record_iterator | tf.io.tf_record_iterator |
| tf.qint16 | tf.dtypes.qint16 |
| tf.qint32 | tf.dtypes.qint32 |
| tf.qint8 | tf.dtypes.qint8 |
| tf.quantize | tf.quantization.quantize |
| tf.quantize_v2 | tf.quantization.quantize_v2 |
| tf.quint16 | tf.dtypes.quint16 |
| tf.quint8 | tf.dtypes.quint8 |
| tf.random_crop | tf.image.random_crop |
| tf.random_gamma | tf.random.gamma |
| tf.random_normal | tf.random.normal |
| tf.random_poisson | tf.random.poisson |
| tf.random_shuffle | tf.random.shuffle |
| tf.random_uniform | tf.random.uniform |
| tf.real | tf.math.real |
| tf.realdiv | tf.math.realdiv |
| tf.reduce_all | tf.math.reduce_all |
| tf.reduce_any | tf.math.reduce_any |
| tf.reduce_join | tf.math.reduce_join |
| tf.reduce_logsumexp | tf.math.reduce_logsumexp |
| tf.reduce_max | tf.math.reduce_max |
| tf.reduce_mean | tf.math.reduce_mean |
| tf.reduce_min | tf.math.reduce_min |
| tf.reduce_prod | tf.math.reduce_prod |
| tf.reduce_sum | tf.math.reduce_sum |
| tf.round | tf.math.round |
| tf.saturate_cast | tf.dtypes.saturate_cast |
| tf.saved_model.builder.SavedModelBuilder | tf.saved_model.SavedModelBuilder |
| tf.saved_model.constants.ASSETS_DIRECTORY | tf.saved_model.ASSETS_DIRECTORY |
| tf.saved_model.constants.ASSETS_KEY | tf.saved_model.ASSETS_KEY |
| tf.saved_model.constants.LEGACY_INIT_OP_KEY | tf.saved_model.LEGACY_INIT_OP_KEY |
| tf.saved_model.constants.MAIN_OP_KEY | tf.saved_model.MAIN_OP_KEY |
| tf.saved_model.constants.SAVED_MODEL_FILENAME_PB | tf.saved_model.SAVED_MODEL_FILENAME_PB |
| tf.saved_model.constants.SAVED_MODEL_FILENAME_PBTXT | tf.saved_model.SAVED_MODEL_FILENAME_PBTXT |
| tf.saved_model.constants.SAVED_MODEL_SCHEMA_VERSION | tf.saved_model.SAVED_MODEL_SCHEMA_VERSION |
| tf.saved_model.constants.VARIABLES_DIRECTORY | tf.saved_model.VARIABLES_DIRECTORY |
| tf.saved_model.constants.VARIABLES_FILENAME | tf.saved_model.VARIABLES_FILENAME |
| tf.saved_model.loader.load | tf.saved_model.load |
| tf.saved_model.loader.maybe_saved_model_directory | tf.saved_model.maybe_saved_model_directory |
| tf.saved_model.main_op.main_op_with_restore | tf.saved_model.main_op_with_restore |
| tf.saved_model.signature_constants.CLASSIFY_INPUTS | tf.saved_model.CLASSIFY_INPUTS |
| tf.saved_model.signature_constants.CLASSIFY_METHOD_NAME | tf.saved_model.CLASSIFY_METHOD_NAME |
| tf.saved_model.signature_constants.CLASSIFY_OUTPUT_CLASSES | tf.saved_model.CLASSIFY_OUTPUT_CLASSES |
| tf.saved_model.signature_constants.CLASSIFY_OUTPUT_SCORES | tf.saved_model.CLASSIFY_OUTPUT_SCORES |
| tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY | tf.saved_model.DEFAULT_SERVING_SIGNATURE_DEF_KEY |
| tf.saved_model.signature_constants.PREDICT_INPUTS | tf.saved_model.PREDICT_INPUTS |
| tf.saved_model.signature_constants.PREDICT_METHOD_NAME | tf.saved_model.PREDICT_METHOD_NAME |
| tf.saved_model.signature_constants.PREDICT_OUTPUTS | tf.saved_model.PREDICT_OUTPUTS |
| tf.saved_model.signature_constants.REGRESS_INPUTS | tf.saved_model.REGRESS_INPUTS |
| tf.saved_model.signature_constants.REGRESS_METHOD_NAME | tf.saved_model.REGRESS_METHOD_NAME |
| tf.saved_model.signature_constants.REGRESS_OUTPUTS | tf.saved_model.REGRESS_OUTPUTS |
| tf.saved_model.signature_def_utils.build_signature_def | tf.saved_model.build_signature_def |
| tf.saved_model.signature_def_utils.classification_signature_def | tf.saved_model.classification_signature_def |
| tf.saved_model.signature_def_utils.is_valid_signature | tf.saved_model.is_valid_signature |
| tf.saved_model.signature_def_utils.predict_signature_def | tf.saved_model.predict_signature_def |
| tf.saved_model.signature_def_utils.regression_signature_def | tf.saved_model.regression_signature_def |
| tf.saved_model.tag_constants.GPU | tf.saved_model.GPU |
| tf.saved_model.tag_constants.SERVING | tf.saved_model.SERVING |
| tf.saved_model.tag_constants.TPU | tf.saved_model.TPU |
| tf.saved_model.tag_constants.TRAINING | tf.saved_model.TRAINING |
| tf.saved_model.utils.build_tensor_info | tf.saved_model.build_tensor_info |
| tf.saved_model.utils.get_tensor_from_tensor_info | tf.saved_model.get_tensor_from_tensor_info |
| tf.scalar_mul | tf.math.scalar_mul |
| tf.serialize_many_sparse | tf.io.serialize_many_sparse |
| tf.serialize_sparse | tf.io.serialize_sparse |
| tf.set_random_seed | tf.random.set_random_seed |
| tf.sign | tf.math.sign |
| tf.space_to_batch | tf.nn.space_to_batch |
| tf.space_to_depth | tf.nn.space_to_depth |
| tf.sparse_add | tf.sparse.add |
| tf.sparse_concat | tf.sparse.concat |
| tf.sparse_fill_empty_rows | tf.sparse.fill_empty_rows |
| tf.sparse_mask | tf.sparse.mask |
| tf.sparse_maximum | tf.sparse.maximum |
| tf.sparse_merge | tf.sparse.merge |
| tf.sparse_minimum | tf.sparse.minimum |
| tf.sparse_placeholder | tf.sparse.placeholder |
| tf.sparse_reduce_max | tf.sparse.reduce_max |
| tf.sparse_reduce_max_sparse | tf.sparse.reduce_max_sparse |
| tf.sparse_reduce_sum | tf.sparse.reduce_sum |
| tf.sparse_reduce_sum_sparse | tf.sparse.reduce_sum_sparse |
| tf.sparse_reorder | tf.sparse.reorder |
| tf.sparse_reset_shape | tf.sparse.reset_shape |
| tf.sparse_reshape | tf.sparse.reshape |
| tf.sparse_retain | tf.sparse.retain |
| tf.sparse_segment_mean | tf.sparse.segment_mean |
| tf.sparse_segment_sqrt_n | tf.sparse.segment_sqrt_n |
| tf.sparse_segment_sum | tf.sparse.segment_sum |
| tf.sparse_slice | tf.sparse.slice |
| tf.sparse_softmax | tf.sparse.softmax |
| tf.sparse_split | tf.sparse.split |
| tf.sparse_tensor_dense_matmul | tf.sparse.matmul |
| tf.sparse_tensor_to_dense | tf.sparse.to_dense |
| tf.sparse_to_indicator | tf.sparse.to_indicator |
| tf.sparse_transpose | tf.sparse.transpose |
| tf.sqrt | tf.math.sqrt |
| tf.square | tf.math.square |
| tf.string | tf.dtypes.string |
| tf.string_split | tf.strings.split |
| tf.subtract | tf.math.subtract |
| tf.tables_initializer | tf.initializers.tables_initializer |
| tf.tanh | tf.math.tanh, tf.nn.tanh |
| tf.train.match_filenames_once | tf.io.match_filenames_once |
| tf.train.write_graph | tf.io.write_graph |
| tf.truediv | tf.math.truediv |
| tf.truncated_normal | tf.random.truncated_normal |
| tf.truncatediv | tf.math.truncatediv |
| tf.truncatemod | tf.math.truncatemod |
| tf.uint16 | tf.dtypes.uint16 |
| tf.uint32 | tf.dtypes.uint32 |
| tf.uint64 | tf.dtypes.uint64 |
| tf.uint8 | tf.dtypes.uint8 |
| tf.unsorted_segment_mean | tf.math.unsorted_segment_mean |
| tf.unsorted_segment_sqrt_n | tf.math.unsorted_segment_sqrt_n |
| tf.variant | tf.dtypes.variant |
| tf.verify_tensor_all_finite | tf.debugging.verify_tensor_all_finite |





# Appendix 2: Deprecated Endpoints

In addition to symbols in this table, we plan to deprecate all symbols under
`tf.logging` (See *Deprecated namespaces* section above).

| Symbol that will be removed | Replacement |
:-------------- |:---------------------------------------------------- |
| tf.COMPILER_VERSION | replace with tf.version.COMPILER_VERSION |
| tf.CXX11_ABI_FLAG | replace with tf.sysconfig.CXX11_ABI_FLAG |
| tf.Event | replace with tf.summary.Event |
| tf.GIT_VERSION | replace with tf.version.GIT_VERSION |
| tf.GRAPH_DEF_VERSION | replace with tf.version.GRAPH_DEF_VERSION |
| tf.GRAPH_DEF_VERSION_MIN_CONSUMER | replace with tf.version.GRAPH_DEF_VERSION_MIN_CONSUMER |
| tf.GRAPH_DEF_VERSION_MIN_PRODUCER | replace with tf.version.GRAPH_DEF_VERSION_MIN_PRODUCER |
| tf.HistogramProto | replace with tf.summary.HistogramProto |
| tf.MONOLITHIC_BUILD | replace with tf.sysconfig.MONOLITHIC_BUILD |
| tf.OpError | replace with tf.errors.OpError |
| tf.PaddingFIFOQueue | replace with tf.io.PaddingFIFOQueue |
| tf.PriorityQueue | replace with tf.io.PriorityQueue |
| tf.QueueBase | replace with tf.io.QueueBase |
| tf.RandomShuffleQueue | replace with tf.io.RandomShuffleQueue |
| tf.SparseConditionalAccumulator | replace with tf.sparse.SparseConditionalAccumulator |
| tf.SparseFeature | replace with tf.io.SparseFeature |
| tf.SummaryMetadata | replace with tf.summary.SummaryMetadata |
| tf.VERSION | replace with tf.version.VERSION |
| tf.accumulate_n | replace with tf.math.accumulate_n |
| tf.angle | replace with tf.math.angle |
| tf.assert_greater_equal | replace with tf.debugging.assert_greater_equal |
| tf.assert_integer | replace with tf.debugging.assert_integer |
| tf.assert_less_equal | replace with tf.debugging.assert_less_equal |
| tf.assert_near | replace with tf.debugging.assert_near |
| tf.assert_negative | replace with tf.debugging.assert_negative |
| tf.assert_non_negative | replace with tf.debugging.assert_non_negative |
| tf.assert_non_positive | replace with tf.debugging.assert_non_positive |
| tf.assert_none_equal | replace with tf.debugging.assert_none_equal |
| tf.assert_positive | replace with tf.debugging.assert_positive |
| tf.assert_proper_iterable | replace with tf.debugging.assert_proper_iterable |
| tf.assert_rank_at_least | replace with tf.debugging.assert_rank_at_least |
| tf.assert_rank_in | replace with tf.debugging.assert_rank_in |
| tf.assert_same_float_dtype | replace with tf.debugging.assert_same_float_dtype |
| tf.assert_scalar | replace with tf.debugging.assert_scalar |
| tf.assert_type | replace with tf.debugging.assert_type |
| tf.betainc | replace with tf.math.betainc |
| tf.bincount | replace with tf.math.bincount |
| tf.ceil | replace with tf.math.ceil |
| tf.cholesky | replace with tf.linalg.cholesky |
| tf.cholesky_solve | replace with tf.linalg.cholesky_solve |
| tf.confusion_matrix | replace with tf.train.confusion_matrix |
| tf.conj | replace with tf.math.conj |
| tf.cross | replace with tf.linalg.cross |
| tf.cumprod | replace with tf.math.cumprod |
| tf.decode_base64 | replace with tf.io.decode_base64 |
| tf.decode_compressed | replace with tf.io.decode_compressed |
| tf.decode_csv | replace with tf.io.decode_csv |
| tf.decode_json_example | replace with tf.io.decode_json_example |
| tf.depth_to_space | replace with tf.nn.depth_to_space |
| tf.deserialize_many_sparse | replace with tf.io.deserialize_many_sparse |
| tf.diag_part | replace with tf.linalg.tensor_diag_part |
| tf.digamma | replace with tf.math.digamma |
| tf.encode_base64 | replace with tf.io.encode_base64 |
| tf.erf | replace with tf.math.erf |
| tf.erfc | replace with tf.math.erfc |
| tf.expm1 | replace with tf.math.expm1 |
| tf.extract_image_patches | replace with tf.image.extract_image_patches |
| tf.fake_quant_with_min_max_args | replace with tf.quantization.fake_quant_with_min_max_args |
| tf.fake_quant_with_min_max_args_gradient | replace with tf.quantization.fake_quant_with_min_max_args_gradient |
| tf.fake_quant_with_min_max_vars | replace with tf.quantization.fake_quant_with_min_max_vars |
| tf.fake_quant_with_min_max_vars_gradient | replace with tf.quantization.fake_quant_with_min_max_vars_gradient |
| tf.fake_quant_with_min_max_vars_per_channel | replace with tf.quantization.fake_quant_with_min_max_vars_per_channel |
| tf.fake_quant_with_min_max_vars_per_channel_gradient | replace with tf.quantization.fake_quant_with_min_max_vars_per_channel_gradient |
| tf.fft | replace with tf.spectral.fft |
| tf.fft2d | replace with tf.spectral.fft2d |
| tf.fft3d | replace with tf.spectral.fft3d |
| tf.floordiv | replace with tf.math.floordiv |
| tf.floormod | replace with tf.math.floormod |
| tf.get_seed | replace with tf.random.get_seed |
| tf.global_norm | replace with tf.linalg.global_norm |
| tf.glorot_normal_initializer | replace with tf.initializers.glorot_normal |
| tf.ifft | replace with tf.spectral.ifft |
| tf.ifft2d | replace with tf.spectral.ifft2d |
| tf.ifft3d | replace with tf.spectral.ifft3d |
| tf.igamma | replace with tf.math.igamma |
| tf.igammac | replace with tf.math.igammac |
| tf.imag | replace with tf.math.imag |
| tf.invert_permutation | replace with tf.math.invert_permutation |
| tf.is_finite | replace with tf.debugging.is_finite |
| tf.is_inf | replace with tf.debugging.is_inf |
| tf.is_non_decreasing | replace with tf.debugging.is_non_decreasing |
| tf.is_numeric_tensor | replace with tf.debugging.is_numeric_tensor |
| tf.is_strictly_increasing | replace with tf.debugging.is_strictly_increasing |
| tf.lbeta | replace with tf.math.lbeta |
| tf.lgamma | replace with tf.math.lgamma |
| tf.log_sigmoid | replace with tf.math.log_sigmoid |
| tf.logical_xor | replace with tf.math.logical_xor |
| tf.manip.batch_to_space_nd | replace with tf.batch_to_space_nd |
| tf.manip.gather_nd | replace with tf.gather_nd |
| tf.manip.reshape | replace with tf.reshape |
| tf.manip.roll | replace with tf.roll |
| tf.manip.scatter_nd | replace with tf.scatter_nd |
| tf.manip.space_to_batch_nd | replace with tf.space_to_batch_nd |
| tf.manip.tile | replace with tf.tile |
| tf.matching_files | replace with tf.io.matching_files |
| tf.matrix_band_part | replace with tf.linalg.matrix_band_part |
| tf.matrix_determinant | replace with tf.linalg.det |
| tf.matrix_diag | replace with tf.linalg.diag |
| tf.matrix_diag_part | replace with tf.linalg.diag_part |
| tf.matrix_inverse | replace with tf.linalg.matrix_inverse |
| tf.matrix_set_diag | replace with tf.linalg.set_diag |
| tf.matrix_solve | replace with tf.linalg.solve |
| tf.matrix_solve_ls | replace with tf.linalg.matrix_solve_ls |
| tf.matrix_transpose | replace with tf.linalg.transpose |
| tf.matrix_triangular_solve | replace with tf.linalg.triangular_solve |
| tf.nn.log_uniform_candidate_sampler | replace with tf.random.log_uniform_candidate_sampler |
| tf.nn.uniform_candidate_sampler | replace with tf.random.uniform_candidate_sampler |
| tf.orthogonal_initializer | replace with tf.initializers.orthogonal_initializer |
| tf.parse_tensor | replace with tf.io.parse_tensor |
| tf.polygamma | replace with tf.math.polygamma |
| tf.python_io.TFRecordCompressionType | replace with tf.io.TFRecordCompressionType |
| tf.python_io.TFRecordOptions | replace with tf.io.TFRecordOptions |
| tf.qr | replace with tf.linalg.qr |
| tf.quantize_v2 | replace with tf.quantization.quantize_v2 |
| tf.quantized_concat | replace with tf.quantization.quantized_concat |
| tf.random_gamma | replace with tf.random.random_gamma |
| tf.random_poisson | replace with tf.random.random_poisson |
| tf.read_file | replace with tf.io.read_file |
| tf.real | replace with tf.math.real |
| tf.realdiv | replace with tf.math.realdiv |
| tf.reciprocal | replace with tf.math.reciprocal |
| tf.reduce_join | replace with tf.math.reduce_join |
| tf.regex_replace | replace with tf.strings.regex_replace |
| tf.rint | replace with tf.math.rint |
| tf.rsqrt | replace with tf.math.rsqrt |
| tf.saved_model.constants.ASSETS_DIRECTORY | replace with tf.saved_model.ASSETS_DIRECTORY |
| tf.saved_model.constants.ASSETS_KEY | replace with tf.saved_model.ASSETS_KEY |
| tf.saved_model.constants.LEGACY_INIT_OP_KEY | replace with tf.saved_model.LEGACY_INIT_OP_KEY |
| tf.saved_model.constants.MAIN_OP_KEY | replace with tf.saved_model.MAIN_OP_KEY |
| tf.saved_model.constants.SAVED_MODEL_FILENAME_PB | replace with tf.saved_model.SAVED_MODEL_FILENAME_PB |
| tf.saved_model.constants.SAVED_MODEL_FILENAME_PBTXT | replace with tf.saved_model.SAVED_MODEL_FILENAME_PBTXT |
| tf.saved_model.constants.SAVED_MODEL_SCHEMA_VERSION | replace with tf.saved_model.SAVED_MODEL_SCHEMA_VERSION |
| tf.saved_model.constants.VARIABLES_DIRECTORY | replace with tf.saved_model.VARIABLES_DIRECTORY |
| tf.saved_model.constants.VARIABLES_FILENAME | replace with tf.saved_model.VARIABLES_FILENAME |
| tf.saved_model.loader.maybe_saved_model_directory | replace with tf.saved_model.maybe_saved_model_directory |
| tf.saved_model.main_op.main_op | replace with tf.saved_model.main_op |
| tf.saved_model.main_op.main_op_with_restore | replace with tf.saved_model.main_op_with_restore |
| tf.saved_model.signature_constants.CLASSIFY_INPUTS | replace with tf.saved_model.CLASSIFY_INPUTS |
| tf.saved_model.signature_constants.CLASSIFY_METHOD_NAME | replace with tf.saved_model.CLASSIFY_METHOD_NAME |
| tf.saved_model.signature_constants.CLASSIFY_OUTPUT_CLASSES | replace with tf.saved_model.CLASSIFY_OUTPUT_CLASSES |
| tf.saved_model.signature_constants.CLASSIFY_OUTPUT_SCORES | replace with tf.saved_model.CLASSIFY_OUTPUT_SCORES |
| tf.saved_model.signature_constants.PREDICT_INPUTS | replace with tf.saved_model.PREDICT_INPUTS |
| tf.saved_model.signature_constants.PREDICT_METHOD_NAME | replace with tf.saved_model.PREDICT_METHOD_NAME |
| tf.saved_model.signature_constants.PREDICT_OUTPUTS | replace with tf.saved_model.PREDICT_OUTPUTS |
| tf.saved_model.signature_constants.REGRESS_INPUTS | replace with tf.saved_model.REGRESS_INPUTS |
| tf.saved_model.signature_constants.REGRESS_METHOD_NAME | replace with tf.saved_model.REGRESS_METHOD_NAME |
| tf.saved_model.signature_constants.REGRESS_OUTPUTS | replace with tf.saved_model.REGRESS_OUTPUTS |
| tf.saved_model.signature_def_utils.classification_signature_def | replace with tf.saved_model.classification_signature_def |
| tf.saved_model.signature_def_utils.is_valid_signature | replace with tf.saved_model.is_valid_signature |
| tf.saved_model.signature_def_utils.predict_signature_def | replace with tf.saved_model.predict_signature_def |
| tf.saved_model.signature_def_utils.regression_signature_def | replace with tf.saved_model.regression_signature_def |
| tf.saved_model.tag_constants.GPU | replace with tf.saved_model.GPU |
| tf.saved_model.tag_constants.TPU | replace with tf.saved_model.TPU |
| tf.saved_model.tag_constants.TRAINING | replace with tf.saved_model.TRAINING |
| tf.saved_model.utils.get_tensor_from_tensor_info | replace with tf.saved_model.get_tensor_from_tensor_info |
| tf.segment_max | replace with tf.math.segment_max |
| tf.segment_mean | replace with tf.math.segment_mean |
| tf.segment_min | replace with tf.math.segment_min |
| tf.segment_prod | replace with tf.math.segment_prod |
| tf.segment_sum | replace with tf.math.segment_sum |
| tf.self_adjoint_eig | replace with tf.linalg.self_adjoint_eig |
| tf.self_adjoint_eigvals | replace with tf.linalg.self_adjoint_eigvals |
| tf.serialize_many_sparse | replace with tf.io.serialize_many_sparse |
| tf.serialize_sparse | replace with tf.io.serialize_sparse |
| tf.space_to_batch | replace with tf.nn.space_to_batch |
| tf.space_to_depth | replace with tf.nn.space_to_depth |
| tf.sparse_add | replace with tf.sparse.add |
| tf.sparse_concat | replace with tf.sparse.concat |
| tf.sparse_fill_empty_rows | replace with tf.sparse.fill_empty_rows |
| tf.sparse_mask | replace with tf.sparse.mask |
| tf.sparse_maximum | replace with tf.sparse.maximum |
| tf.sparse_merge | replace with tf.sparse.merge |
| tf.sparse_minimum | replace with tf.sparse.minimum |
| tf.sparse_placeholder | replace with tf.sparse.placeholder |
| tf.sparse_reduce_max | replace with tf.sparse.reduce_max |
| tf.sparse_reduce_max_sparse | replace with tf.sparse.reduce_max_sparse |
| tf.sparse_reduce_sum | replace with tf.sparse.reduce_sum |
| tf.sparse_reduce_sum_sparse | replace with tf.sparse.reduce_sum_sparse |
| tf.sparse_reorder | replace with tf.sparse.reorder |
| tf.sparse_reset_shape | replace with tf.sparse.reset_shape |
| tf.sparse_reshape | replace with tf.sparse.reshape |
| tf.sparse_segment_mean | replace with tf.sparse.segment_mean |
| tf.sparse_segment_sqrt_n | replace with tf.sparse.segment_sqrt_n |
| tf.sparse_segment_sum | replace with tf.sparse.segment_sum |
| tf.sparse_slice | replace with tf.sparse.slice |
| tf.sparse_softmax | replace with tf.sparse.softmax |
| tf.sparse_split | replace with tf.sparse.split |
| tf.sparse_tensor_dense_matmul | replace with tf.sparse.matmul |
| tf.sparse_to_dense | replace with tf.sparse.to_dense which takes SparseTensor
object |
| tf.sparse_to_indicator | replace with tf.sparse.to_indicator |
| tf.sparse_tensor_to_dense | replace with tf.sparse.to_dense |
| tf.sparse_transpose | replace with tf.sparse.transpose |
| tf.string_join | replace with tf.strings.join |
| tf.string_strip | replace with tf.strings.strip |
| tf.string_to_hash_bucket | replace with tf.strings.to_hash_bucket |
| tf.string_to_hash_bucket_fast | replace with tf.strings.to_hash_bucket_fast |
| tf.string_to_hash_bucket_strong | replace with tf.strings.to_hash_bucket_strong |
| tf.substr | replace with tf.strings.substr |
| tf.svd | replace with tf.linalg.svd |
| tf.trace | replace with tf.linalg.trace |
| tf.train.VocabInfo | replace with tf.estimator.VocabInfo |
| tf.train.match_filenames_once | replace with tf.io.match_filenames_once |
| tf.truncatediv | replace with tf.math.truncatediv |
| tf.truncatemod | replace with tf.math.truncatemod |
| tf.uniform_unit_scaling_initializer | replace with tf.initializers.uniform_unit_scaling |
| tf.unsorted_segment_max | replace with tf.math.unsorted_segment_max |
| tf.unsorted_segment_mean | replace with tf.math.unsorted_segment_mean |
| tf.unsorted_segment_min | replace with tf.math.unsorted_segment_min |
| tf.unsorted_segment_prod | replace with tf.math.unsorted_segment_prod |
| tf.unsorted_segment_sqrt_n | replace with tf.math.unsorted_segment_sqrt_n |
| tf.unsorted_segment_sum | replace with tf.math.unsorted_segment_sum |
| tf.variance_scaling_initializer | replace with tf.initializers.variance_scaling |
| tf.verify_tensor_all_finite | replace with tf.debugging.verify_tensor_all_finite |
| tf.write_file | replace with tf.io.write_file |
| tf.zeta | replace with tf.math.zeta |


