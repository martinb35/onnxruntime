class PytorchTrainer(object):
    r"""Pytorch frontend for ONNX Runtime training

    Entry point that exposes the C++ backend of ORT as a Pytorch frontend.

    Args:
        model (torch.nn.Module or onnx.ModelProto): either a PyTorch or ONNX model.
            When a PyTorch model and :py:attr:`loss_fn` are specified, :py:attr:`model` and :py:obj:`loss_fn` are combined.
            When a ONNX model is provided, the loss is identified by the flag :py:obj:`is_loss=True` in one of the :py:attr:`.model_desc.outputs` entries.
        model_desc (dict): model input and output description.
            This is used to identify inputs and outputs and their shapes, so that ORT can generate back propagation graph, plan memory allocation for
            training, and perform optimizations.
            :py:attr:`model_desc` must be consistent with the training :py:attr:`model` and have the following (:py:obj:`dict`) schema
            :py:obj:`{ 'inputs': [tuple(name, shape)], 'outputs': [tuple(name, shape, is_loss)]}`.
            :py:attr:`name` is a string representing name of input or output of the model.
            For :py:obj:`model_desc['inputs']` entries, :py:attr:`name` must match input names of the original PyTorch model's :py:meth:`torch.nn.Module.forward` method.
            For :py:obj:`model_desc['outputs']` entries, the order must match the original PyTorch's output as returned by :py:meth:`torch.nn.Module.forward` method.
            :py:attr:`shape` is a list of string or integers that describes the shape of the input/output.
            Each dimension size can be either a string or an int. String means the dimension size is dynamic, while integers mean static dimensions.
            An empty list implies a scalar.
            Lastly, :py:attr:`is_loss` is a boolean (default is False) that flags if this output is considered a loss.
            ORT backend needs to know which output is loss in order to generate back propagation graph.
            Loss output must be specified when either :py:attr:`loss_fn` is specified or when loss is embedded in the model.
            Note that only one loss output is supported per model.
        optimizer_config (.optim._OptimizerConfig): optimizer config.
            One of :py:class:`.optim.Adam`, :py:class:`.optim.Lamb` or :py:class:`.optim.SGD`.
        loss_fn (default is None): a PyTorch loss function.
            It takes two inputs [prediction, label] and output a loss tensor.
            If provided, :py:attr:`loss_fn` is combined with the PyTorch :py:attr:`model` to form a combined PyTorch model.
            Inputs to the combined PyTorch model are concatenation of the :py:attr:`model`'s input and :py:attr:`loss_fn`'s label input.
            Outputs of the combined PyTorch model are concatenation of :py:attr:`loss_fn`'s loss output and :py:attr:`model`'s outputs.
        options (ORTTrainerOptions, default is None): options for additional features.

    Example:
        .. code-block:: python

            model = BertForPreTraining(config)
            model_desc = {
                "inputs": [
                    ("input_ids", ["batch", "max_seq_len_in_batch"]),
                    ("attention_mask", ["batch", "max_seq_len_in_batch"]),
                    ("token_type_ids", ["batch", "max_seq_len_in_batch"]),
                    ("masked_lm_labels", ["batch", "max_seq_len_in_batch"]),
                    ("next_sentence_label", ["batch", 1])
                ],
                "outputs": [
                    ("loss", [], True),
                ],
            }
            optim_config = optim.Lamb(param_groups = [ { 'params' : ['model_param0'], 'alpha' : 0.8, 'beta' : 0.7},
                                                       { 'params' : ['model_param1' , 'model_param_2'], 'alpha' : 0.0}
                                                     ],
                                      alpha=0.9, beta=0.999)
            ort_trainer = ORTTrainer(model, model_desc, optim_config)
    """
    def __init__(self, model, model_desc, optim_config, loss_fn=None, options=None):
        pass

    def __call__(self, *args, **kwargs):
        pass

    def eval(self):
        pass

    def eval_step(self, *input, **kwargs):
        r"""Evaluation step method

        Args:
            *input: Arbitrary arguments that are used as model input
            **kwargs: Arbitrary keyword arguments that are used as model input

        Returns:
            ordered :py:obj:`list` with model outputs as described by :py:attr:`ORTTrainer.model_desc`
        """
        pass

    def load_state_dict(self, state_dict, strict=False):
        pass

    def save_as_onnx(self, path):
        pass

    def state_dict(self):
        pass

    def train_step(self, *input, **kwargs):
        r"""Train step method

        After forward pass, an ordered list with all outputs described at :py:attr:`ORTTrainer.model_desc` is returned.
        Additional information relevant to the train step is updated at :py:attr:`ORTTrainer._train_step_info`. See :py:class:`ORTTrainerOptions` for details.

        Args:
            *input: Arbitrary arguments that are used as model input
            **kwargs: Arbitrary keyword arguments that are used as model input

        Returns:
            ordered :py:obj:`list` with model outputs as described by :py:attr:`ORTTrainer.model_desc`
        """
        pass

    def train(self):
        pass

