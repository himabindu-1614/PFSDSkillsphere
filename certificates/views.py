from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Certificate
from .forms import CertificateForm



def certificates(request):
    user = request.user
    certs = Certificate.objects.filter(user=user)

    # SEARCH
    q = request.GET.get('q')
    if q:
        certs = certs.filter(title__icontains=q)

    # CATEGORY FILTER
    category = request.GET.get('category')
    if category:
        certs = certs.filter(category=category)

    # VERIFIED FILTER (optional)
    verified = request.GET.get('verified')
    if verified == 'yes':
        certs = certs.filter(is_verified=True)
    elif verified == 'no':
        certs = certs.filter(is_verified=False)

    return render(request, 'certificates/certificates_list.html', {
        'certificates': certs
    })


@login_required
def dashboard(request):

    certs=Certificate.objects.filter(
        user=request.user
    )

    total=certs.count()

    verified=certs.filter(
        is_verified=True
    ).count()

    expired=0
    expiring_count=0

    return render(
        request,
        'certificates/dashboard.html',
        {
         'total':total,
         'verified':verified,
         'expired':expired,
         'expiring_count':expiring_count
        }
    )


@login_required
def add_certificate(request):

    if request.method=="POST":

        form=CertificateForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            cert=form.save(
                commit=False
            )

            cert.user=request.user
            cert.save()

            messages.success(
                request,
                "Certificate saved successfully"
            )

            return redirect(
                'certificates'
            )

    else:
        form=CertificateForm()

    return render(
      request,
      'certificates/add_certificate.html',
      {'form':form}
    )


@login_required
def edit_certificate(request,pk):

    cert=get_object_or_404(
        Certificate,
        id=pk,
        user=request.user
    )

    if request.method=="POST":

        form=CertificateForm(
            request.POST,
            request.FILES,
            instance=cert
        )

        if form.is_valid():
            form.save()
            return redirect(
                'certificates'
            )

    else:
        form=CertificateForm(
            instance=cert
        )

    return render(
        request,
        'certificates/add_certificate.html',
        {'form':form}
    )


@login_required
def delete_certificate(request,pk):

    cert=get_object_or_404(
      Certificate,
      id=pk,
      user=request.user
    )

    cert.delete()

    return redirect(
       'certificates'
    )


@login_required
def preview_certificate(request,pk):

    cert=get_object_or_404(
       Certificate,
       id=pk,
       user=request.user
    )

    return render(
      request,
      'certificates/preview.html',
      {'cert':cert}
    )


def profile(request):
    user = request.user

    certs = Certificate.objects.filter(user=user)

    total = certs.count()
    verified = certs.filter(is_verified=True).count()

    from datetime import date, timedelta
    today = date.today()

    expiring = certs.filter(
        expiry_date__gte=today,
        expiry_date__lte=today + timedelta(days=30)
    ).count()

    expired = certs.filter(
        expiry_date__lt=today
    ).count()

    return render(request, 'certificates/profile.html', {
        'total': total,
        'verified': verified,
        'expiring': expiring,
        'expired': expired
    })