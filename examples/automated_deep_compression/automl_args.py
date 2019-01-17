def add_automl_args(argparser, arch_choices=None, enable_pretrained=False):
    """
    Helper function to make it easier to add command-line arguments for AMC to any application.

    Arguments:
        argparser (argparse.ArgumentParser): Existing parser to which to add the arguments
    """
    group = argparser.add_argument_group('AutoML Compression Arguments')
    group.add_argument('--amc-protocol', choices=["mac-constrained",
                                                  "param-constrained",
                                                  "accuracy-guaranteed",
                                                  "mac-constrained-experimental"],
                       default="mac-constrained", help='Compression-policy search protocol')
    group.add_argument('--amc-ft-epochs', type=int, default=1,
                       help='The number of epochs to fine-tune each discovered network')
    group.add_argument('--amc-save-chkpts', action='store_true', default=False,
                       help='Save checkpoints of all discovered networks')
    group.add_argument('--amc-action-range',  type=float, nargs=2, default=[0.0, 0.80],
                       help='Density action range (a_min, a_max)')
    group.add_argument('--amc-heatup-epochs', type=int, default=100,
                       help='The number of epochs for heatup/exploration')
    group.add_argument('--amc-training-epochs', type=int, default=300,
                       help='The number of epochs for training/exploitation')
    group.add_argument('--amc-reward-every-step', action='store_true', default=False,
                       help='Compute the reward at every step')
    group.add_argument('--amc-target-density', type=float,
                       help='Target density of the network we are seeking')
    # group.add_argument('--amc-thinning', action='store_true', default=False,
    #                    help='Perform netowrk thinning after altering each layer')
